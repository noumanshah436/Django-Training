from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm

# https://docs.djangoproject.com/en/4.2/topics/class-based-views/intro/

# HTTP GET in a view function would look something like:


def my_view(request):
    if request.method == "GET":
        # <view logic>
        return HttpResponse("result")


# In a class-based view, this would become:
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse("result")

# *****************************

# While a minimal class-based view does not require any class attributes
#  to perform its job, class attributes are useful in many class-based designs,
#  and there are two ways to configure or set class attributes.

# The first is the standard Python way of subclassing and overriding attributes
#  and methods in the subclass.
# So that if your parent class had an attribute greeting like this:


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


# You can override that in a subclass:
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"

# Another option is to configure class attributes as keyword arguments
#   to the as_view() call in the URLconf:

# urlpatterns = [
#     path("about/", GreetingView.as_view(greeting="G'day")),
# ]

# *****************************

# Handling forms with class-based views

# A basic function-based view that handles forms may look something like this:


def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})

    return render(request, 'form_template.html', {'form': form})


class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
