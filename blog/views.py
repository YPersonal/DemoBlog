#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import User
# Create your views here.

def index(request):
    users = User.objects
    return HttpResponse('Hello Word!')#render(request, 'blog/user_info.html',{'users':users})



