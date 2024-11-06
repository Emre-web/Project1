from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=70)
    imageUrl = models.CharField(max_length=50 )
    date = models.DateTimeField()
    isActive = models.BooleanField(default=True)
     

    def __str__(self):
        return f"{self.title} {self.description} {self.imageUrl} {self.date} {self.isActive}"
            