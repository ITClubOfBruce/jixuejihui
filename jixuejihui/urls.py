import xadmin
from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from django.views.static import serve
from jixuejihui.settings import MEDIA_ROOT
from users.views import logout_view,LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetPwdView,ModifyPwdView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('logout/',logout_view,name='logout'),
    path('login/',LoginView.as_view(),name='login'),
    path('captcha/',include('captcha.urls')),
    path('register/',RegisterView.as_view(),name='register'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/',ResetPwdView.as_view(),name='reset_pwd'),
    path('modify_pwd/',ModifyPwdView.as_view(),name='modify_pwd'),
    re_path('media/(?P<path>.*)',serve,{'document_root':MEDIA_ROOT}),
    path('org/',include('organization.urls',namespace="org")),
    path('course/',include('course.urls',namespace="course")),
    # path('users/',include('users.urls',namespace="users")),
]
