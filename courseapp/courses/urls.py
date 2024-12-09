from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('create-course', views.create_course, name="create_course"), 
    path('<slug:slug>/', views.details, name="course_details"),  # Ensure trailing slash
    path('course-edit/<int:id>/', views.course_edit, name="course_edit"), 
    path('course-delete/<int:id>/', views.course_delete, name="course_delete"), 
    path('upload', views.upload, name="image"), 
    path('course-list', views.course_list, name="course_list"),
    path('Category/<slug:slug>/', views.getCoursesByCategory, name='courses_by_category'),  # Ensure trailing slash
]