from django.shortcuts import render, redirect
from myfirstapp.forms import EmployeeForm


def index(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/myfirstapp/')
    else:
        form = EmployeeForm()
        return render(request, "index.html", {'form': form})
