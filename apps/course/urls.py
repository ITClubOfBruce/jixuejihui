from django.urls import path,re_path

from .views import CourseListView,CourseDetailView

app_name = "course"
urlpatterns = [
    path('list/',CourseListView.as_view(),name="course_list"),
    re_path('detail/(?P<course_id>\d+)/',CourseDetailView.as_view(),name="course_detail")
]