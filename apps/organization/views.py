from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
from .models import CourseOrg,CityDict

class OrgView(View):
    '''
    课程机构
    '''
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        all_citys = CityDict.objects.all()

        # 获取前端传过来的城市id
        city_id = request.GET.get('city')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 获取到前端传过来的机构类别ct
        category = request.GET.get('ct')
        if category:
            all_orgs = all_orgs.filter(category=category)
        org_onums = all_orgs.count()

        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            # 如果用户请求的页码号不是整数，显示第一页
            page = 1
        p = Paginator(all_orgs,2,request=request)
        page_orgs = p.page(page)

        context = {
            "all_orgs": page_orgs,
            "org_onums": org_onums,
            "all_citys": all_citys,
            "city_id":city_id,
            "category":category
        }
        return render(request,'organization/org-list.html',context)