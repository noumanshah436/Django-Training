from django.urls import path

from .views import EmployeeCreate, EmployeeDetail
from .views import EmployeeRetrieve, EmployeeUpdate, EmployeeDelete

app_name = 'employee_app'
urlpatterns = [
    path('', EmployeeCreate.as_view(), name='employee_create'),
    path('retrieve/', EmployeeRetrieve.as_view(), name='employee_retrieve'),
    path('<int:pk>', EmployeeDetail.as_view(), name='employee_detail'),
    path('<int:pk>/update/', EmployeeUpdate.as_view(), name='employee_update'),
    path('<int:pk>/delete/', EmployeeDelete.as_view(), name='employee_delete')
]
