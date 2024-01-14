from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='hello'),
]


# http://127.0.0.1: 8000/myfirstapp/index
