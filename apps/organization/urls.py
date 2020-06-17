from organization.views import OrgView,UserAskView,OrgDetailHomeView,OrgDetailCourseView,OrgDescDetailView
from django.urls import path,re_path

app_name = "organization"

urlpatterns = [
    path('list/',OrgView.as_view(),name='org_list'),
    path('add_ask/',UserAskView.as_view(),name="add_ask"),
    re_path('home/(?P<org_id>\d+)/',OrgDetailHomeView.as_view(),name="org_home"),
    re_path('course/(?P<org_id>\d+)/',OrgDetailCourseView.as_view(),name="org_course"),
    re_path('desc/(?P<org_id>\d+)/', OrgDescDetailView.as_view(), name="org_desc"),
]