from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def index(requests):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(requests,'blog/index.html',context)

def single_blog(requests,pk):
    blog = Blog.objects.get(pk=pk)
    return render(requests,'blog/single-blog.html',{'blog':blog})
