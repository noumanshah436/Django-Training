from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default ->  required=True

    class Meta:
        model = User
        # when we say form.save(),  it should save in that User model
        fields = ['username', 'email', 'password1', 'password2']
        # fields that will be shown on the form
