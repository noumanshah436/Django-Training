from django.shortcuts import render, redirect

# Create your views here.
from django import forms
from django.utils import timezone
from myfirstapp.forms import MyCommentForm   # .forms also works


def index(request):

    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            # print("model_instance: ", model_instance)  ->  model_instance:  name 
            # print("time: ",timezone.now()) -> time:  2021-07-15 22: 28: 49.363881+00: 00
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/myfirstapp/index')
    else:
        form = MyCommentForm()
        return render(request, "my_template.html", {'form': form})
