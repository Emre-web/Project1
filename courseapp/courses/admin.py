from django.contrib import admin
from .models import Category, Course
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'imageUrl', 'date', 'isActive')
    list_display_links = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('date', 'isActive')
    list_editable = ('isActive',)
    search_fields = ('title', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',),}
