from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

class OrgView(View):
    '''
    课程机构
    '''
    def get(self,request):
        return render(request,'organization/org-list.html')