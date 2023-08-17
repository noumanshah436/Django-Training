from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default ->  required=True

    class Meta:
        model = User
        # when we say form.save(),  it should save in that User model
        fields = ['username', 'email', 'password1', 'password2']
        # fields that will be shown on the form


"""
model form allows us to create a form
that will work with a specific database model
"""


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
