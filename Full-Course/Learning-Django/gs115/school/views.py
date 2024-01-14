from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Function based view    //  http://127.0.0.1:8000/homefun/
def homefun(request):
    return render(request, 'school/home.html')


# Class based View   // http://127.0.0.1:8000/homecl/
class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html')

# ###################################################

# render html page 

#  http://127.0.0.1:8000/aboutfun/

def aboutfun(request):     
    context = {'msg': "Welcome to Manish's Home page" }
    return render(request, 'school/about.html', context)

# http://127.0.0.1:8000/aboutcl/

class AboutClassView(View):
    def get(self, request):
        context = {'msg': "Welcome to Manish's Home page" }
        return render(request, 'school/about.html', context)

# ###################################################

# render form

# http://127.0.0.1:8000/contactfun/
def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank You!!! Form Submitted")
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form': form})

# http://127.0.0.1:8000/contactcl/
class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name =form.cleaned_data['name']
            print(name)
            return HttpResponse(f"Thank You {name}!!! Form Submitted")

# ###################################################

# http://127.0.0.1:8000/newscl/
def newsfun(request, template_name):
    template_name = template_name
    context = {'info': "CBI enquiry WHy I earn Less Mioney"}
    return render(request, template_name, context)

# http://127.0.0.1:8000/newscl1/
class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info': "CBI enquiry why I learn Less Money"}
        return render(request, self.template_name, context)
