from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from datetime import datetime


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
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug": "python-kursu",
            "date": datetime(2024,11,3),
            "is-active": True
                    },
                    {
            "title" : "React.js Kursu",
            "instructor": " Mehmet Taha",
            "description": "React.js Kütüphanesini öğrenmek için bu kursa katılın.",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug": "React.js-kursu",
            "date": datetime(2024,11,3),
            "is-active": True
                    },
                    {
            "title" : "Sql Kursu",
            "instructor": "Ali Veli",
            "description": "Sql dilini öğrenmek için bu kursa katılın.",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug": "Sql-kursu",
            "date": datetime(2024,11,3),
            "is-active": True
                    },
    ],
        "categories": [
       { "id": 1, "name": "programlama", "slug": "programlama" },
       { "id": 2, "name": "web-gelistirme", "slug": "web-gelistirme"},
       { "id": 3, "name": "veritabani", "slug": "veritabani" },
          ]
    
}
def index(request):
    kurslar = db["courses"]
    kategoriler = db["categories"]


    return render(request,'coursespages/index.html',{
        'categories': kategoriler,
        'courses': kurslar

    })

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} Kursu Detayları')

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