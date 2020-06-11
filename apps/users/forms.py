from django import forms

# 登录表单验证
class LoginForm(forms.Form):
    # 用户名和密码不能为空,密码的长度不能小于6位
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6)