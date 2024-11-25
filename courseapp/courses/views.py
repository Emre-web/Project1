from django.shortcuts import get_object_or_404, redirect, render
from courses.forms import CourseCreateForm
from .models import Course, Category
from django.core.paginator import Paginator


def index(request):
    kurslar = Course.objects.filter(isActive=True, isHome=True)
    kategoriler = Category.objects.all()

    return render(request,'coursespages/index.html',{
        'categories': kategoriler,
        'coursespages': kurslar

    })

def create_course(request):
        if request.method == 'POST':
             form = CourseCreateForm(request.POST)

             if form.is_valid():
                kurs = Course(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                imageUrl=form.cleaned_data["imageUrl"],
                slug=form.cleaned_data["slug"])
                kurs.save()
                return redirect('/kurslar')

        
        form = CourseCreateForm()
        return render(request, 'coursespages/create-course.html',{"form":form})


def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by('-date')
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")

    paginator = Paginator(kurslar, 2)
    page_number = request.GET.get('page', 1)
    page_object = paginator.get_page(page_number)

    return render(request, 'coursespages/search.html', {
        'categories': kategoriler,
        'courses': page_object,  # Updated to use page_object
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
    


    paginator = Paginator(kurslar, 2)
    page_number = request.GET.get('page',1) 
    page_object = paginator.page(page_number)


    return render(request, 'coursespages/list.html', {
        'categories': kategoriler,
        'page_object': page_object,
        'seciliCategory': slug
    })