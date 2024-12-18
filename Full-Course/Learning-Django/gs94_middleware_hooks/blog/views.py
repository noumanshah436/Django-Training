from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


# http://localhost:8000/
def home(request):
    print("I am Home View")
    return HttpResponse("This is Home Page")


# http://localhost:8000/excp
def excp(request):
    print("I am Excp View")
    a = 10 / 0
    return HttpResponse("This is Excp Page")


# http://localhost:8000/user
def user_info(request):
    print("I am User Info View")
    context = {"name": "Rahul"}
    return TemplateResponse(request, "blog/user.html", context)
