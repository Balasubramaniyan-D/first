from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def srujana(request):
    return HttpResponse('<marquee><h1>Emira Thinnava, Em Chesthunnavura')

def revi(request):
    return HttpResponse('<marquee><b>Mama Kutty, Long drive Polama')

def ramar(request):
    return HttpResponse('<marquee><h2>Ennama Neenga Ippadi Panrengaley ma')