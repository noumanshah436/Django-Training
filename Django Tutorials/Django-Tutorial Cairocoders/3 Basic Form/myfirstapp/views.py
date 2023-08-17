from django.shortcuts import render, redirect

# Create your views here.
from django import forms
from myfirstapp.forms import StudentForm


def index(request):
    student = StudentForm()
    return render(request, "form.html", {'form': student})
