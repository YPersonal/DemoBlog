#-*- coding: utf-8 -*-
from django.db import models
import time, uuid
# Create your models here.


class User(models.Model):
    #__table__ ='users' Django 中表名不是这么命名的，
    # 可参考下面的Meta 类


    id = models.AutoField(primary_key=True)
    email =models.EmailField(max_length=254)
    passwd = models.CharField(max_length=50)
    admin = models.BooleanField()
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500,blank=True)
    create_at = models.FloatField(default=time.time())

    class Meta:
        db_table = 'users'



class Blog(models.Model):
    #__table__ = 'blogs'

    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    user_image = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.FloatField(default=time.time())

    class Meta:
        db_table = 'blogs'


class Comment(models.Model):
    #__table__ = 'comments'

    id = models.AutoField(primary_key=True)
    blog_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    user_image = models.CharField(max_length=500)
    content = models.TextField()
    create_at = models.FloatField(default=time.time())

    class Meta:
        db_table = 'comments'



