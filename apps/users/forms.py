from django import forms
from captcha.fields import CaptchaField

# 登录表单验证
class LoginForm(forms.Form):
    # 用户名和密码不能为空,密码的长度不能小于6位
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6)


# 注册表单的验证
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6)
    # 验证码
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

# 找回密码
class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})


# 重置密码的表单验证
class ModifyPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True,min_length=6,max_length=20)
    password2 = forms.CharField(required=True,min_length=6,max_length=20)












