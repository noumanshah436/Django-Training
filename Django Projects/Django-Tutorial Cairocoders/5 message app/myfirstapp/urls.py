from django.urls import path, include
from . import views

urlpatterns = [
    # path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),

]


# http://127.0.0.1: 8000/myfirstapp/   ******
# http://127.0.0.1: 8000/myfirstapp/contact
