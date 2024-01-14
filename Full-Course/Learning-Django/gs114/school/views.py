from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Function Based View  ( http://127.0.0.1:8000/func/ )
def myview(request):
    return HttpResponse('<h1>Function Based View</h1>')


# Class Based View    ( http://127.0.0.1:8000/cl/ )
class MyView(View):
    name = 'Sonam'
    def get(self, request):
        # return HttpResponse('<h1>Class Based View - GET</h1>')
        return HttpResponse(self.name)


## Chile class of above created view
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)
