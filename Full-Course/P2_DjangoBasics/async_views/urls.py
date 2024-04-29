from django.urls import path
from .views import home_view, main_view, main_view_async

urlpatterns = [
    path('', home_view, name='home-view'),
    path('sync/', main_view, name='sync-main-view'),
    path('async/', main_view_async, name='async-main-view'),
]
