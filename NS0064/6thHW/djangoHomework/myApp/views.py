from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

def helloWorld(request):
    return HttpResponse("Hello world")

def blog(request):
    blogs = Blog.objects.all()
    description = {'blogs': blogs}
    return render(request, 'myApp/blog.html', description)