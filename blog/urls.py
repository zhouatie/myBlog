from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.blog_title, name='blog_titles')
]