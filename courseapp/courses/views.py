from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

data = {
    "programlama": "programlama kursları",
    "web-gelistirme": "web geliştirme kursları",
    "veritabani": "veritabanı kursları",
}

def kurslar(request):
    return HttpResponse('Kurslar')

def list(request):
    return HttpResponse('list')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} Kursu Detayları')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except KeyError:
        return HttpResponseNotFound("Yanlış Kategori")

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if 0 < category_id <= len(category_list):
        redirect_text = category_list[category_id - 1]

        redirect_url = reverse('courses_by_category', args=[redirect_text])
        return redirect(redirect_url)
    else:
        return HttpResponseNotFound("Yanlış Kategori ID")