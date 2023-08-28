# urls.py
from django.urls import path
from my_class_based_views.views import MyView, GreetingView

urlpatterns = [
    path("about/", MyView.as_view()),
    path("about/", GreetingView.as_view(greeting="G'day")),
]
