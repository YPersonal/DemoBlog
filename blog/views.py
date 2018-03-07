#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import User
from . import models
# Create your views here.

def index(request):
    blogs = models.Blog.objects.all()

    return render(request,'blog/index.html',{"blogs": blogs})
    # # users = User.objects.filter(name='测试人')
    # return HttpResponse('Hello Word! My Email is')#render(request, 'blog/user_info.html',{'users':users})
