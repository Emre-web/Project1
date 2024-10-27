from django.urls import path
from . import views


urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('<kurs_adi>', views.details),
    path('Category/<int:category_id>', views.getCoursesByCategoryId),
    path('Category/<str:category_name>', views.getCoursesByCategory),
]