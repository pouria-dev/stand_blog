from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
    path('' , index , name='home'),
    path('list' , article , name='list'),
    path('about' , about , name='about'),
    path('detail/<str:slug>' , article_detail , name='detail'),
    path('category/<str:slug>' , category_detail , name='category'),
    path('contact' , contact , name="contact"),
    path('search' , search , name='search_system'),
]