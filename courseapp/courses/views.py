from django.shortcuts import get_object_or_404, redirect, render
from courses.forms import CourseCreateForm, CourseEditForm
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
             form = CourseCreateForm(request.POST, request.FILES)

             if form.is_valid():
                form.save()
                return redirect('/kurslar')

        
        form = CourseCreateForm()
        return render(request, 'coursespages/create-course.html',{"form":form})

def course_list(request):
    kurslar = Course.objects.all()

    return render(request,'coursespages/course-list.html',{
        'coursespages': kurslar

    })

def course_edit(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        form = CourseEditForm(request.POSTT, request.FILES, instance=course)
        if form.is_valid(): #bu kısımda formun doğruluğunu kontrol ediyoruz. 
            form.save()
            return redirect('course_list')  # Updated to use the correct URL name
    else:
        form = CourseEditForm(instance=course)

    return render(request, "coursespages/edit-course.html", { 'form': form })

def course_delete(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.delete()
        return redirect('course_list')

    return render(request, 'coursespages/course-delete.html', {'course': course })

def upload(request):
    if request.method == 'POST':
       uploated_image = request.FILES['image']
       handle_uploaded_file(uploated_image)
       return render(request, "coursespages/success.html")
    return render(request, 'coursespages/upload.html')

def handle_uploaded_file(file):
    with open("temp/" + file.name,"wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
         


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