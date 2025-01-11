from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog
from .forms import blogForm

def helloWorld(request):
    return HttpResponse("Hello world")

def blog(request):
    blogs = Blog.objects.all()
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = blogForm()
    context = {
        'blogs': blogs,
        'form': form
    }
    return render(request, 'myApp/blog.html', context)


def createBlog(request):
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = blogForm()
    return render(request, 'myApp/createBlog.html', {'form': form})

