from django.urls import path,re_path
from django.shortcuts import HttpResponse,render,redirect
from django.http import JsonResponse
from django.conf.urls import  include
from django.conf.urls import url

from app01 import  views
from app01 import orm
urlpatterns = [
    path('index_db/',views.index_db),
    path('show_usr_info/',views.show_usr_info),
    path('index/',orm.index),
    path('custom/',orm.custom),
    path('test/',views.test),
]