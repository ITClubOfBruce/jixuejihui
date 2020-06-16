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
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        # 获取前端传过来的城市id
        city_id = request.GET.get('city','')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 获取到前端传过来的机构类别ct
        category = request.GET.get('ct','')
        if category:
            all_orgs = all_orgs.filter(category=category)
        org_onums = all_orgs.count()

        # 根据学习人数和课程数进行排序
        sort = request.GET.get("sort","")
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by("-students")
            elif sort == 'courses':
                all_orgs = all_orgs.order_by("-course_nums")
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
            "category":category,
            "hot_orgs":hot_orgs,
            "sort":sort
        }
        return render(request,'organization/org-list.html',context)




# 处理我要咨询的请求的视图
from .forms import UserAskForm
from operation.models import UserAsk

class UserAskView(View):
    '''
    用户咨询
    '''
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = UserAsk()
            user_ask.name = request.POST.get('name')
            user_ask.mobile = request.POST.get('mobile')
            user_ask.course_name = request.POST.get('course_name')
            user_ask.save()