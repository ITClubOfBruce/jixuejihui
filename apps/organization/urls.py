from organization.views import OrgView,UserAskView
from django.urls import path,re_path

app_name = "organization"

urlpatterns = [
    path('list/',OrgView.as_view(),name='org_list'),
    path('add_ask/',UserAskView.as_view(),name="add_ask")
]