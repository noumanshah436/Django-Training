"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""

login and logout are django built-in class based views.
We just need to make login and logout templates ( also set their path ) .
and in login template, we  need to display the form in it provided by django .

********

if we do not specify template_name inside as_view , it will show admin login and logout pages.

********

by default if the auth_views.LoginView ( http://127.0.0.1:8000/login )is successfull, 
it redirect it to this view (route/function):
http://127.0.0.1:8000/accounts/profile .

********

by default if the auth_views.LogoutView( http://127.0.0.1:8000/logout )
will show admin logout page and can take us to admin login page, 
but we will make our own user logout page and add link to user-login page

********

one is admin login page ( built-in ) and the other is 
our own user login page ( in users/login.html ), 

********

this is the dafault location where django looks for login routes
http://127.0.0.1:8000/accounts/profile .
we can change it by specifying this in setting.py file

LOGIN_URL = 'login'

"""
