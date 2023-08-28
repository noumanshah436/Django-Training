from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import NameForm, ContactForm


# https://docs.djangoproject.com/en/4.0/topics/forms/         forms
# https://docs.djangoproject.com/en/4.0/ref/forms/fields/      form fields

def my_forms(request):
    return render(request, 'my_forms/my_form.html')


# http://localhost:8000/my_forms/get_name/
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['your_name']
            # redirect to a new URL:
            return HttpResponse(name)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'my_forms/my_form.html', {'form': form})


# http://localhost:8000/my_forms/get_contact/
def get_contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            profile = {
                "subject": subject,
                "message": message,
                "sender": sender,
                "cc_myself": cc_myself
            }
            return JsonResponse(profile)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    # return render(request, 'my_forms/my_form.html', {'form': form})
    return render(request, 'my_forms/rendering_form_manually.html',
                  {'form': form})
