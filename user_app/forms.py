""" Develop specific forms

 forms:

    -Login and register user
    -Dashboard user admin

 """



from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.template.defaulttags import widthratio


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









class DashBoard_Form(forms.Form):
    class Meta:
        model = User
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

    def save(self):
        pass
