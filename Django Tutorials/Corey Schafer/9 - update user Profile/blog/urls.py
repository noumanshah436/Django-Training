from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]


# names can be used to redirect to this specific route as
# return redirect('blog-home')
