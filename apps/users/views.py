import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout

@csrf_exempt
def user_login(request):
    response = HttpResponse('test', content_type='application/json')
    if request.method == 'GET':
        response = HttpResponse('test')
        response.set_cookie('my_cookie',"Bruce")
        return response
    data = request.body
    req = data.decode('utf-8')
    req = json.loads(req)

    username = req['username']
    password = req['password']

    # 调用authenticate校检用户名和密码
    user = authenticate(username=username,password=password)
    print(user.username, user.password)
    # 如果user存在，说明验证成功
    if user is not None:
        login(request,user)
        resp = {"status":"success"}
        response.content = json.dumps(resp)
        response.status_code = 200
        response["Access-Control-Allow-Credentials"] = "true"
        # response["Access-Control-Allow-Origin"] = "http://localhost:8000"
        response.set_cookie("username", username, 60000)
        response.set_cookie("password", password, 60000)

        return response
        # return HttpResponse(json.dumps(resp),content_type='appication/json')
    else:
        resp = {"status": "fail"}
        return JsonResponse(resp)
        # return HttpResponse(json.dumps(resp),content_type='appication/json')