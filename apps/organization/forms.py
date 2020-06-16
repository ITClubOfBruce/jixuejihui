from django import forms

class UserAskForm(forms.Form):
    name = forms.CharField()
    mobile = forms.CharField()
    course_name = forms.CharField()