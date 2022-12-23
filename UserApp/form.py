from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #declare configuration for the form
        model = User #form.save() will then save to the User model.
        fields = ['username','email','password1','password2']