from django.shortcuts import render

# https://www.youtube.com/watch?v=SxRezJzcQJg&list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6&index=67 

# https://learnbatta.com/blog/django-custom-path-converters-17/      for uname

# Create your views here.

# http://127.0.0.1:8000/student/session/2014
def show_details(request, year):
    return render(request, 'enroll/show.html', {'yr': year})


def user_detail(request, uname):
    return render(request, 'enroll/show.html', {'uname': uname})