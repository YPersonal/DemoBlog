#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import User
from . import models
# Create your views here.

def index(request):
    blogs = models.Blog.objects.all()
    return render(request,'blog/index.html',{"blogs": blogs})



def edit(request):
    return render(request,'blog/edit.html')

def edit(request, blog_id=0):
    if blog_id ==0:
        return render(request, 'blog/edit.html')
    else:
        blog = models.Blog.objects.get(id=blog_id)
        return render(request,'blog/edit.html',{"blog":blog})

def content(request,blog_id):
    print("##############################")
    print('the blog id is ',blog_id)
    blog = models.Blog.objects.get(id=blog_id)
    return render(request,'blog/content.html',{'blog':blog})

def eidt_action(request):
    title = request.POST.get("title","TITLE")
    content = request.POST.get("content","CONTENT")
    summary = request.POST.get("summary","summary")
    blog_id = request.POST.get("blog_id",0)
    if blog_id==0:
        models.Blog.objects.create(name=title, summary=summary, content=content)
    else:
        blog=models.Blog.objects.get(id=blog_id)#._do_update(name=title, summary=summary, content=content)
        blog.name =title
        blog.summary = summary
        blog.content = content
        blog.save()


    blogs = models.Blog.objects.all()
    return render(request, 'blog/index.html', {"blogs": blogs})
