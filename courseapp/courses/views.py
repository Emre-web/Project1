from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from .models import Course, Category
from django.core.paginator import Paginator


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

     
def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by('-date')
    kategoriler = Category.objects.all()


    paginator = Paginator(kurslar, 1)
    page_number = request.GET.get('page',1) 
    page_object = paginator.page(page_number)


    return render(request, 'coursespages/index.html', {
        'categories': kategoriler,
        'page_object': page_object,
        'seciliCategory': slug
    })