from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from datetime import datetime
from .models import Course, Category

data = {
    "programlama": "programlama kursları",
    "web-gelistirme": "web geliştirme kursları",
    "veritabani": "veritabanı kursları",
}

db = {
    "courses": [
            {
            "title" : "Python Kursu",
            "instructor": "Ahmet Mehmet",
            "description": "Python programlama dilini öğrenmek için bu kursa katılın.",
            "imageUrl":"1.jpg",
            "slug": "python-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
                    },
                    {
            "title" : "React.js Kursu",
            "instructor": " Mehmet Taha",
            "description": "React.js Kütüphanesini öğrenmek için bu kursa katılın.",
            "imageUrl":"2.jpg", 
            "slug": "React.js-kursu",
            "date": datetime(2024,11,3),
            "isActive": True,
            "isUpdated": True
                    },
                    {
            "title" : "Sql Kursu",
            "instructor": "Ali Veli",
            "description": "Sql dilini öğrenmek için bu kursa katılın.",
            "imageUrl":"3.jpg",
            "slug": "Sql-kursu",
            "date": datetime(2024,11,3),
            "isActive": True,
            "isUpdated": True
                    },
    ],
        "categories": [
       { "id": 1, "name": "programlama", "slug": "programlama" },
       { "id": 2, "name": "web-gelistirme", "slug": "web-gelistirme"},
       { "id": 3, "name": "veritabani", "slug": "veritabani" },
          ]
    
}
def index(request):
    kurslar = Course.objects.filter(isActive=True)
    kategoriler = Category.objects.all()

    # for kurs in db["courses"]:
    #     if kurs["isActive"] == True:    
    #         kurslar.append(kurs)

    return render(request,'coursespages/index.html',{
        'categories': kategoriler,
        'courses': kurslar

    })


def details(request, slug):   
  
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course 
          }
    return render(request, 'coursespages/details.html', context)

     
def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'coursespages/courses.html', {
        'category': category_name,
        'category_text': category_text
        })
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