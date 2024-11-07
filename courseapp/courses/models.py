from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    
            
    def __str__(self):
        return f"{self.name}"  
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=70)
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",blank=True, editable=False, null=False,unique=True, db_index=True)
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)
     
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
     return f"{self.title} {self.description} {self.imageUrl} {self.date} {self.isActive}"



