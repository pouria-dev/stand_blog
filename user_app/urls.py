from django.urls import  path
from . import views


app_name = 'user'
urlpatterns= [

    path('login' , views.login_user , name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_user , name='register'),
    path('profile', views.user_panel, name='profile'),

]