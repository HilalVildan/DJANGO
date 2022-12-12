from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello this is our home page..")


def students(request):
    return HttpResponse("Ali, Veli, Cemal")