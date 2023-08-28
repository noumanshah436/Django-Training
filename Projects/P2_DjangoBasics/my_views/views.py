from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.utils import timezone
from .models import Post, Car
from django.contrib.auth.models import User
from django.views import generic
from .forms import PostForm


# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World</h1>")


def get_user_by_id(request, id):
    user = User.objects.get(id=id)
    profile = {
        "name": user.username,
        "email": user.email
    }
    return JsonResponse(profile)


def index2(request):
    return render(request, "my_views/index.html")


# http://localhost:8000/index3/
def index3(request):
    # Strings
    my_name = "Nouman"

    # Integers
    my_age = 30

    # html string
    my_html = "<h1>This is some HTML</h1>"

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C", "Rust"]

    res = [['Adam', '334', 'Ford'], [
        'Steve', '130', 'Porsche'], ['Dave', '510', 'Ford']]

    # Dictionaries
    friends = {
        "Ali": 43,
        "Humza": 28,
        "Syed": 26,
        "Farhan": 23,
        "Fatima": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    bool_var = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    date = datetime.utcnow()

    suspicious = "<script>alert('NEVER TRUST USER INPUT!')</script>"

    context = {
        "langs": langs, "res": res, "var1": my_name, "my_age": my_age,
        "friends": friends, "colors": colors, "bool_var": bool_var,
        "GitRemote": GitRemote, "my_remote": my_remote, "repeat": repeat,
        "date": date, "my_html": my_html, "suspicious": suspicious
    }

    return render(request, "my_views/gettingDataFromViews.html", context)


#
def build_in_tags_and_filters(request):
    name = "Nouman"
    langs = ["Python", "JavaScript", "Bash", "Ruby", "C++", "Rust"]
    some_date = datetime(2023, 8, 18, 15, 30, 0)
    utc_date = datetime.utcnow()
    current_datetime = timezone.now()

    context = {
        'name': name, 'langs': langs, "some_date": some_date,
        "utc_date": utc_date, "current_datetime": current_datetime
    }

    return render(request, 'my_views/build_in_tags_and_filters.html', context)


# http://localhost:8000/posts/
def display_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'my_views/posts.html', context)


# http://localhost:8000/newpost/
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post(title=title, content=content, author_id=1)
            post.save()
            return redirect('my_views:posts')
    else:
        form = PostForm()
    return render(request, 'my_views/myForm.html', {'form': form})


# **************************
# generic views
# **************************

class MyCarsIndexView(generic.ListView):
    model = Car

    def get_queryset(self):
        return Car.objects.order_by("model")


class MyCarDetailView(generic.DetailView):
    model = Car
