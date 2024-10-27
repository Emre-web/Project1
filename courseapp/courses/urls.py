from django.urls import path
from . import views
#http://127.0.0.1:8000/client/    => Anasayfa
#http://127.0.0.1:8000/client/home => Anasayfa
#http://127.0.0.1:8000/client/kurslar => Kurslar


urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('kurslar', views.kurslar),
]
