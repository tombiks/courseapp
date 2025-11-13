from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("")

def hakkimizde(request):
    return HttpResponse("hakkımızda sayfası")

def iletisim(request):
    return HttpResponse("iletişim sayfası")

