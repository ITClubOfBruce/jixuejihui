import json

from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except:
            return None

# @csrf_exempt
# def user_login(request):
#     response = HttpResponse('test', content_type='application/json')
#     # 获取Ajax传入的纯json数据
#     data = request.body
#     req = data.decode('utf-8')
#     req = json.loads(req)
#     username = req['username']
#     password = req['password']
#     # 调用authenticate校检用户名和密码
#     user = authenticate(username=username,password=password)
#     print(user.username, user.password)
#     response["Access-Control-Allow-Credentials"] = "true"
#     response["Access-Control-Allow-Origin"] = "http://localhost:5500"
#     response.set_cookie("username",user.username,60*60*24*15)
#     response.set_cookie("password",user.password,60*60*24*15)
#     # 如果user存在，说明验证成功
#     if user is not None:
#         login(request,user)
#         resp = {"status":"success"}
#         response.content = json.dumps(resp)
#         response.status_code = 200
#         return response
#         # return HttpResponse(json.dumps(resp),content_type='appication/json')
#     else:
#         resp = {"status": "fail"}
#         return JsonResponse(resp)
#         # return HttpResponse(json.dumps(resp),content_type='appication/json')

#  FBV的登出,模板中的登出
def logout_view(request):
    logout(request)
    return render(request,'login.html')

from django.views.generic.base import View
from .forms import LoginForm

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户名或者密码错误', 'login_form': login_form})
            else:
                return render(request,'login.html',{'msg':'用户名或者密码错误','login_form':login_form})
        else:
            return render(request,'login.html',{'login_form':login_form})


'''
    注册
'''
from .forms import RegisterForm

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('email')
            # 如果邮箱已经注册过了，就不允许注册了
            if UserProfile.objects.filter(email=username):
                return render(request,'register.html',{'register_form':register_form,'msg':'用户已经存在'})
            password = request.POST.get('password')

            user = UserProfile()
            user.username = username
            user.email = username
            user.is_active = False

            # 对密码进行加密
            user.password = make_password(password)
            user.save()
            # 发送邮件
            send_register_email(username,'register')

            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form})


'''
    激活账号
'''
from .models import EmailVerifyRecord
class ActiveUserView(View):
    def get(self,request,active_code):
        # 查询邮箱验证记录类中是否存在active_code
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request,'active_fail_html')
        return render(request,'login.html')













