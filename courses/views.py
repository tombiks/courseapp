from django.http import HttpResponse
from django.shortcuts import render



def kurslar(request):
    return HttpResponse("kurs listesi")

def details(request):
    return HttpResponse("kurs detay sayfası")

def programlama(request):
    return HttpResponse("programlama sayfası")

def mobiluygulama(request):
    return HttpResponse("mobil uygulama sayfası")


