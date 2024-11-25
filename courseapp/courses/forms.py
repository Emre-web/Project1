from django import forms

from courses.models import Category 

class CourseCreateForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), error_messages={'required': 'Bu alan zorunludur.'})
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}),  max_length= 100, error_messages={'required': 'Bu alan zorunludur.'})
    imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    isActive = forms.BooleanField(required=False)
    isHome = forms.BooleanField(required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    slug = forms.SlugField( widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class": "form-control"}))


    #novalidate ettiğimiz form templkates videosunda