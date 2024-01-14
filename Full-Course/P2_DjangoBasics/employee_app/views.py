# from django.shortcuts import redirect, render
from django.urls import reverse_lazy
# from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class EmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_app:employee_retrieve')


class EmployeeRetrieve(ListView):
    model = Employee


class EmployeeDetail(DetailView):
    model = Employee


class EmployeeUpdate(UpdateView):
    model = Employee
    template_name_suffix = '_update_form'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_app:employee_retrieve')

    # def get_success_url(self):


class EmployeeDelete(DeleteView):
    model = Employee
    # here we can specify the URL
    # to redirect after successful deletion
    success_url = '/'
