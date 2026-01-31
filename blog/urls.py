from django.urls import path
from .views import IndexView , AboutView , CategoryListView , ContactView
from .views import article , article_detail , searching_system

app_name='blog'

urlpatterns = [
    path('' , IndexView.as_view() , name='home'),
    path('about' , AboutView.as_view() , name='about'),
    path('list' , article , name='list'),
    path('detail/<str:slug>' , article_detail , name='detail'),
    path('category/<str:slug>' , CategoryListView.as_view() , name='category'),
    path('contact' , ContactView.as_view() , name="contact"),
    path('search' , searching_system , name='search_system'),
]