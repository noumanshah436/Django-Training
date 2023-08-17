from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.helloworld, name='hello'),
    path('hello/', views.hello, name='hello'),
    path('index/', views.index , name='hello'),

]


# http: // 127.0.0.1: 8000/
# http: // 127.0.0.1: 8000/myfirstapp/
# http: // 127.0.0.1: 8000/myfirstapp/hello/
# http://127.0.0.1: 8000/myfirstapp/index
