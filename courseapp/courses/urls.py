from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name="course_details"),
    path('Category/<int:category_id>', views.getCoursesByCategoryId),
    path('Category/<str:category_name>', views.getCoursesByCategory,name = 'courses_by_category'),] 