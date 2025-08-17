"""
This file for write decorators
"""



from django.urls import reverse
from django.shortcuts import redirect




### This decorator for cheking if user is anonymous , redirect the user to login page
def login_check(func):
    def wrapper(request , *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse("user:login"))
        
        return func(request,*args, **kwargs)
    
    return wrapper