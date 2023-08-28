from django.urls import path
from . import views

#    /my_forms/
# urlpatterns
urlpatterns = [
    path('', views.my_forms, name="my_form"),
    path('get_name/', views.get_name, name="get_name"),
    path('get_contact/', views.get_contact, name="get_contact"),
]
