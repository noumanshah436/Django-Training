# urls.py
from django.urls import path
from my_class_based_views.views import MyView

urlpatterns = [
    path("about/", MyView.as_view()),
]
