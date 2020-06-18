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

        # 设置课程点击数+1
        course.click_nums += 1
        course.save()

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:3]
        else:
            relate_courses = []

        context = {
            "course":course,
            "relate_courses":relate_courses
        }
        return render(request,'course/course-detail.html',context)


from .models import CourseResource

class CourseInfoView(View):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resourses = CourseResource.objects.filter(course=course)
        context = {
            "course":course,
            "all_resourses":all_resourses
        }
        return render(request,'course/course-video.html',context)

# 课程评论
from operation.models import CourseComments

class CourseCommentsView(View):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resourses = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course)

        context = {
            'course':course,
            "all_resourses": all_resourses,
            "all_comments":all_comments
        }
        return render(request,"course/course-comment.html",context)


from .models import Video
class VideoPlayView(View):
    def get(self,request,video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course

        all_resourses = CourseResource.objects.filter(course=course)
        context = {
            'video':video,
            'course':course,
            'all_resourses':all_resourses
        }
        return render(request,'course/course-play.html',context)










