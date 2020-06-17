from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator,PageNotAnInteger,EmptyPage
from .models import Course
# Create your views here.
class CourseListView(View):
    def get(self,request):
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]

        # 得到前端传递过来的sort字段
        sort = request.GET.get('sort','')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by("-students")
            elif sort == 'hot':
                all_courses = all_courses.order_by("-click_nums")

        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses,2,request=request)
        courses = p.page(page)

        context = {
            "all_courses":courses,
            "hot_courses":hot_courses,
            "sort":sort
        }
        return render(request,'course/course-list.html',context)



class CourseDetailView(View):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        context = {
            "course":course,
        }
        return render(request,'course/course-detail.html')















