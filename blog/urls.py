from django.urls import path
from .views import IndexView , AboutView , CategoryListView , ContactView , ArticleListView , LikeArticleView
from .views import  article_detail 

app_name='blog'

urlpatterns = [
    path('' , IndexView.as_view() , name='home'),
    path('about' , AboutView.as_view() , name='about'),
    path('list' , ArticleListView.as_view() , name='list'),
    path('detail/<slug:slug>' , article_detail , name='detail'),
    path('category/<slug:slug>' , CategoryListView.as_view() , name='category'),
    path('contact' , ContactView.as_view() , name="contact"),
    path("like/<slug:slug>", LikeArticleView.as_view(), name="like"),
]