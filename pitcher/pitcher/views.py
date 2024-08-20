# from django.http import HttpResponse

# def hello(request):
#     text = """<h1>Welcome to my App !</h1>"""
#     return HttpResponse(text)




from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello world")