from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login ,logout
from django.urls import  reverse
from django.contrib import  messages
from .forms import DashBoard_Form , Login_Form




def login_user(request):

    if request.user.is_authenticated:
        return redirect('blog:home')

    form = Login_Form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('blog:home')


            else:

                return form.add_error(None , "something went wrong")


    return render(request , 'user_app/login.html' , {'form':form})



def logout_view(request):
    logout(request)


def dashboard(request):
    if request.method == 'POST':
        form = DashBoard_Form(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'You have successfully logged in.')

    else:
        form = DashBoard_Form()
