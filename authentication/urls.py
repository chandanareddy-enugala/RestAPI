from django.urls import path

from .views import user_create
from django.contrib.auth import  auth_views

url_patterns = [
    path("signup/",user_create,name ="signup")
  ]