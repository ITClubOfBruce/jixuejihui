import xadmin
from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from users.views import logout_view,LoginView,RegisterView,ActiveUserView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('logout/',logout_view,name='logout'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active')
]
