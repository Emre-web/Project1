from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True,max_length=50)
            
    def __str__(self):
        return f"{self.name}"  
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=70)
    image = models.ImageField(upload_to='image')
    date = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="", editable=True, null=False, unique=True, db_index=True, max_length=50)
    categories = models.ManyToManyField(Category)

    def __str__(self):
     return f"{self.title} {self.description} {self.image} {self.date} {self.isActive} {self.isHome} {self.slug} {self.categories}"


class UploadModel(models.Model):
    image = models.FileField(upload_to='image')
   
    


