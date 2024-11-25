from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('create-course', views.create_course, name="create_course"),
    path('<slug:slug>/', views.details, name="course_details"),  # Ensure trailing slash
    path('Category/<slug:slug>/', views.getCoursesByCategory, name='courses_by_category'),  # Ensure trailing slash
]