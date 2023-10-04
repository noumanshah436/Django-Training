from django.urls import path, register_converter
from .views import show_details,user_detail
from . import converters

register_converter(converters.UsernamePathConverter, 'username')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('session/<yyyy:year>', show_details, name='detail'),
    path('articles/<username:uname>/', user_detail, name="user_detail")
]

# http://127.0.0.1:8000/student/session/2014

# http://127.0.0.1:8000/student/articles/nouman