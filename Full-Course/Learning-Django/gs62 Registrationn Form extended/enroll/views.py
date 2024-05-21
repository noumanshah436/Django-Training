from django.http import HttpResponse
from django.shortcuts import render

from .utils import (
    send_email,
    send_email_with_attachment,
    notify_admins,
    notify_managers,
    send_templated_email,
)
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.


# http://127.0.0.1:8000/signup/
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully!!!")
            fm.save()
            # send_email()
    else:
        fm = SignUpForm()
    return render(request, "enroll/signup.html", {"form": fm})


# http://localhost:8000/send_email/
def send_email_view(request):
    send_email_with_attachment()
    return HttpResponse("Email sent successfully!")


# http://localhost:8000/notify_admins/
def notify_admins_view(request):
    notify_admins()
    return HttpResponse("Admins notified successfully.")


# http://localhost:8000/notify_managers/
def notify_managers_view(request):
    notify_managers()
    return HttpResponse("Managers notified successfully.")


# http://localhost:8000/send_templated_email
def send_templated_email_view(request):
    send_templated_email()
    return HttpResponse("Templated email sent successfully!")
