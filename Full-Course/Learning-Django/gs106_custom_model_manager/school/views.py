from django.shortcuts import render
from .models import Student

# we create custom model manager to change the default behavior of queryset(return all objects)
# In our custom model manager, we are returning all objects order by name.

def home(request):
    student_data = Student.students.all()
    return render(request, 'school/home.html', {'students': student_data})
