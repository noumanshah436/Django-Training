from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up),
    path('send_email/', views.send_email_view),
    path('notify_admins/', views.notify_admins_view),
    path('send_templated_email/', views.send_templated_email_view),
]
