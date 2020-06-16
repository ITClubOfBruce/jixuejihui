from organization.views import OrgView,UserAskView,OrgDetailHomeView
from django.urls import path,re_path

app_name = "organization"

urlpatterns = [
    path('list/',OrgView.as_view(),name='org_list'),
    path('add_ask/',UserAskView.as_view(),name="add_ask"),
    re_path('home/(?P<org_id>\d+)/',OrgDetailHomeView.as_view(),name="org_home")
]