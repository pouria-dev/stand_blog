from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
    path('' , IndexView.as_view() , name='home'),
    path('about' , AboutView.as_view() , name='about'),
    path('list' , article , name='list'),
    path('detail/<str:slug>' , article_detail , name='detail'),
    path('category/<str:slug>' , category_detail , name='category'),
    path('contact' , contact , name="contact"),
    path('search' , searching_system , name='search_system'),
]