from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Anasayfa')


def iletisim(request):
    return HttpResponse('İletisim') 

def hakkimizda(request):
    return HttpResponse('Hakkımızda')
