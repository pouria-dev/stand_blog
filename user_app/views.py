from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login ,logout
from .forms import Login_Form, Register_Form, User_PanelForm


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
    return redirect('blog:home')



def register_user(request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    form = Register_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)

            login(request, user)

            return redirect('blog:home')

        else:
            form.add_error(None , "something went wrong")

    return render(request , 'user_app/register.html' , {'form':form})




def user_panel(request):
    form = User_PanelForm(instance=request.user)
    if request.method == "POST":
        form = User_PanelForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
    return render(request, "user_app/user_panel.html", context={'form':form})