from django import forms
from .models import Course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug', 'categories',)
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'slug': 'Slug'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #attr içindeki class form-control bootstrapin form elemanlarını düzgün göstermesi için
        }
        error_messages = {
            'title': {
                'required': 'Bu alan zorunludur.',
                'max_length': 'En fazla 50 karakter olmalıdır.',
            },
            'description': {
                'required': 'Bu alan zorunludur.',
            },
            'slug': {
                'required': 'Bu alan zorunludur.',
            },
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug', 'categories', 'isActive', 'isHome')
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'slug': 'Slug'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #attr içindeki class form-control bootstrapin form elemanlarını düzgün göstermesi için
        }
        error_messages = {
            'title': {
                'required': 'Bu alan zorunludur.',
                'max_length': 'En fazla 50 karakter olmalıdır.',
            },
            'description': {
                'required': 'Bu alan zorunludur.',
            },
            'slug': {
                'required': 'Bu alan zorunludur.',
            },
        }

class UploadForm(forms.Form):
    image = forms.FileField()
