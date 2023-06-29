from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'username','password1','password2')