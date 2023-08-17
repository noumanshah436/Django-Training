from django.urls import path
from . import views

#    /myforms/
# urlpatterns
urlpatterns = [
    path('', views.my_forms, name="myForm"),
    path('GetName/', views.get_name, name="getName"),
    path('GetContact/', views.get_contact, name="getContact"),
]
