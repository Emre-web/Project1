from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse('Kurslar')

def list(request):
    return HttpResponse('list')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} Kursu Detayları')

def getCoursesByCategory(request, category_name):
        text = ""


        if(category_name == 'programlama'):
             text = 'Programlama Kursları'

        elif(category_name == 'web-gelistirme'):
                text = 'Web Geliştirme Kursları'
        
        elif(category_name == 'veritabani'):
                text = 'Veritabanı Kursları'

        else:
                text = 'Yanlış Kategori'

        return HttpResponse(text)

def getCoursesByCategoryId(request, category_id):
      return HttpResponse(f'Kategori ID: {category_id}')

