""" Develop specific forms

 forms:

    -Login and register user
    -Dashboard user admin

 """
from importlib.metadata import requires

from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError



class Login_Form(forms.Form):
    username = forms.CharField(max_length=120 , widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'input100'}))



    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    self.add_error('password','password is incorrect')



            except User.DoesNotExist:
                self.add_error('username','username does not exist')






class Register_Form(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100' , 'placeholder':'<PASSWORD>'}))

    class Meta:
        model = User
        fields = ('username','email','password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100' , 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'input100' , 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'input100' , 'placeholder': 'Password'}),
        }




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False





    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        password2 = clean_data.get('password2')

        if password and password2 and password != password2:
            self.add_error('password2', 'Passwords must match')

        return clean_data


    def clean_username(self):
        user_name = self.cleaned_data.get('username')

        user = User.objects.filter(username=user_name).exists()

        if user :
            raise ValidationError('Username already taken')



        return user_name




class DashBoard_Form(forms.Form):
    class Meta:
        model = User
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

    def save(self):
        pass
