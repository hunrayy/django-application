from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")