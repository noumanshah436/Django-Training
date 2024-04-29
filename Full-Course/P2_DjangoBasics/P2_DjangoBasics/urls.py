"""
URL configuration for P2_DjangoBasics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# http://localhost:8000/contact/
def contact(request):
    return HttpResponse("<h1>My Number: 03424556029</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_views.urls')),
    path("polls/", include("polls.urls")),
    path('employees/', include("employee_app.urls")),
    path('bookshelf/', include("bookshelf.urls")),
    path('task_manager/', include("task_manager.urls")),
    path('contact/', contact, name="contact"),
    path('my_forms/', include('my_forms.urls')),
    path('async_views/', include('async_views.urls')),
]
