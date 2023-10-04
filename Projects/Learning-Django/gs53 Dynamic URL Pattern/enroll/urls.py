from django.urls import path
from .views import show_details, home, show_subdetails


urlpatterns = [
    path('', home, {'check': 'Nouman'}, name='home'),
    path('<int:my_id>/', show_details, name='detail'),
    path('<int:my_id>/<int:my_subid>', show_subdetails, name='subdetail'),
]

# http://127.0.0.1:8000/student/