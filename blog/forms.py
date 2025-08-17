from django import forms
from django.core.validators import ValidationError
from .models import Comment
from django.contrib.auth import aauthenticate
from django.contrib.auth.models import User


class Contact_Form(forms.Form):
    name = forms.CharField(max_length=10 , label="Name")
    text = forms.CharField(widget=forms.Textarea , label="Text")
    email = forms.EmailField(label="Email:")


    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')

        if name == text :
            raise ValidationError("name and text are same" , code='name and text')


    def clean_name(self):
        name = self.cleaned_data.get('name')

        if "p" in name:
            return  ValidationError("no")
        

class Comment_Form(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']








