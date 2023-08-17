from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def helloworld(request):
    return HttpResponse('<h1>hello World</h1>')


def hello(request):
    today = datetime.datetime.now().date()
    print(today)
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})


"""
In setting.py of main project:

'DIRS': [os.path.join(BASE_DIR,'templates')]

STATIC_URL = '/static/'

In HTML file to access static files
  {% load static %}

"""


def index(request):
    template = loader.get_template('index.html')  # getting our template
    name = {  # Variable Example
        'student': 'Syed Nouman'
    }
    # rendering the template in HttpResponse
    return HttpResponse(template.render(name))

# def index(request):
#    now = datetime.datetime.now()
#    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
#    return HttpResponse(html)    # rendering the template in HttpResponse
