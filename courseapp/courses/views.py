from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse('Kurslar')

def list(request):
    return HttpResponse('list')

def details(request):
    return HttpResponse('Detaylar')

def programlama(request):
    return HttpResponse('Programlama')

