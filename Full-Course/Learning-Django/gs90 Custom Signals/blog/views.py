from django.shortcuts import render, HttpResponse
from blog import signals
from blog.user_visit_signal import user_visit_signal
from django.utils import formats
from django.http import JsonResponse
import datetime


# http://127.0.0.1:8000
def home(request):
    signals.notification.send(sender=None, request=request, user=["Geeky", "Shows"])
    return HttpResponse("This is Home Page")


# custom user_visit_signal
# https://medium.com/@mansha99/django-drf-signals-custom-signals-model-signals-enforcing-business-rules-729fc2e22c7c


# http://127.0.0.1:8000/hello_world/
def hello_world(request):
    message = "Hello World"
    date_time = datetime.datetime.now()
    date_time = formats.date_format(date_time, "SHORT_DATETIME_FORMAT")
    ip = get_client_ip(request=request)
    device = request.META["HTTP_USER_AGENT"]
    # sending signal
    user_visit_signal.send(sender=request, date_time=date_time, ip=ip, device=device)
    return HttpResponse(message)


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
