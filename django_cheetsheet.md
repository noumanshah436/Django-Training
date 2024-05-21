Certainly! Here's a structured and comprehensive Django cheat sheet based on the content provided:

---

## My Beloved Django Cheat Sheet

### Project Setup

**Create and access project folder:**
```sh
mkdir project_name
cd project_name
```

**Create and activate Python virtual environment:**
```sh
python3 -m venv venv
source venv/bin/activate
# Deactivate with: deactivate
```

**Install Django:**
```sh
pip install django~=3.1.0
```

**Start a new Django project:**
```sh
django-admin startproject config .
```

**Create a new app:**
```sh
python manage.py startapp app_name
```

### Migrations

**Create migration files:**
```sh
python manage.py makemigrations
```

**Apply migrations:**
```sh
python manage.py migrate
```

### Superuser

**Create a superuser:**
```sh
python manage.py createsuperuser
```

### Server

**Run the development server:**
```sh
python manage.py runserver
# Access at http://127.0.0.1:8000
```

### Dependencies

**Create a requirements file:**
```sh
pip freeze > requirements.txt
```

**Install from requirements file:**
```sh
pip install -r requirements.txt
```

### Other Commands

**Django shell:**
```sh
python manage.py shell
```

**Collect static files:**
```sh
python manage.py collectstatic
```

**Dump data to JSON:**
```sh
python manage.py dumpdata app_name > app_name.json
```

**Load data from JSON:**
```sh
python manage.py loaddata app_name.json
```

### Project Configuration

**Add app to `settings.py`:**
```python
INSTALLED_APPS = [
    ...,
    'app_name',
]
```

**Templates:**

- App templates folder: `app_name/templates/app_name/`
- Project templates folder: `project_name/templates/`

**Settings for templates in `settings.py`:**
```python
TEMPLATES = [
    {
        ...,
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```

**Static files:**

- Create static folder: `project_name/static/`
- Settings in `settings.py`:
    ```python
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / 'static']
    STATIC_ROOT = 'static_root'
    ```

### Models

**Define a model (`models.py`):**
```python
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    credit = models.FloatField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    TYPE_CHOICES = (
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
        ('Student', 'Student'),
    )

    type = models.CharField(choices=TYPE_CHOICES, max_length=50)

    def __str__(self):
        return self.name
```

### Admin

**Register a model in `admin.py`:**
```python
from .models import Blog
admin.site.register(Blog)
```

**Customize admin panel:**
```python
from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    fields = ("title", "description")
    list_display = ("title", "description")
    list_display_links = ("title",)
    ordering = ("date_created",)
    search_fields = ("title", "description")

admin.site.register(Blog, BlogAdmin)
```

### URLs

**Project URLs (`urls.py`):**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_name.urls')),
]
```

**App URLs (`app_name/urls.py`):**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.index, name='posts.index'),
    path('posts/create/', views.create, name='posts.create'),
    path('posts/<int:id>/', views.show, name='posts.show'),
    path('posts/<int:id>/edit/', views.edit, name='posts.edit'),
    path('posts/<int:id>/delete/', views.delete, name='posts.delete'),
]
```

**Static files in URLs:**
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### Views

**Function-based views (`views.py`):**
```python
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index(request):
    # Get all Posts
    posts = Post.objects.all()

    # Render app template with context
    return render(request, 'appfolder/index.html', {'posts': posts})

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'appfolder/show.html', {'post': post})

def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        # optionally we can access form data with form.cleaned_data['first_name']
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('/posts')

    return render(request, 'appfolder/create.html', {'form': form)

def edit(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('/posts')

    return render(request, 'appfolder/edit.html', {'form': form)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/posts')
```

**Class-based views (`views.py`):**
```python
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class LandingPageView(TemplateView):
    template_name = 'landing.html'

    # Optional: Change context data dict
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Landing Page'
        return context

class PostsListView(ListView):
    queryset = Post.objects.all()

  # Optional
    # context_object_name = "posts" (default: post_list)
    # template_name = 'posts.html' (default: posts/post_list.html) 

class PostsDetailView(DetailView):
    model = Post # object var in template

  # Optional
    # template_name = 'post.html' (default: posts/post_detail.html)


class PostsCreateView(CreateView):
    form_class = PostForm

    template_name = 'posts/post_create.html' # no default value

    def get_success_url(self):
        return reverse('posts-list')

    # Optional: Overwrite form data (before save)
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            from.instance.author = self.request.user

        return super().form_valid(form)

class PostsUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_update.html'

    def get_success_url(self):
        return reverse('post-list')

    # Optional: Change context data dict
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Update'
        return context


class PostsDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts-list')

# Urls.py route declaration
path('<int:pk>/update/', PostsUpdateView.as_view(), name='post-update')
```

Certainly! Here's a concise cheat sheet for various Django topics covered in your detailed outline:

## Django Template Basics

### Template Directory
- Templates are stored in `project_folder/templates` or `app_folder/templates/app_name/*.html`

### Extending Templates
```html
{% extends 'base.html' %}
{% block content %}     
{% endblock %}
```

### Including Templates
```html
{% include 'header.html' %}
```

### Template Logic
```html
{% if user.username == 'Mike' %}
    <p>Hello Admin</p>   
{% else %}   
    <p>Hello User</p>
{% endif %}
```

### Looping
```html
{% for product in products %}   
  <p>The product name is {{ product }}</p>
{% endfor %}
```

### Variable Display
```html
{{ var_name }}
```

### Variable Formatting
```html
{{ title | lower }}
{{ blog.post | truncatewords:50 }}
{{ order.date | date:"D M Y" }}
{{ list_items | slice:":3" }}
{{ total | default:"nil" }}
```

### Current Path
```html
{{ request.path }}
```

### URL by Name with Parameter
```html
{% url 'posts.delete' id=post.id %}
```

### Static Files
```html
{% load static %}
{% static 'css/main.css' %}
```

## Model Managers and Querysets

### CRUD Operations
- **Create and Save**:
```python
Article.objects.create(name='Item 1', price=19.95)
article = Article(user=user, name='Item 1', price=19.95)
article.save()
```

- **Read**:
```python
Article.objects.all()
Article.objects.get(id=1)
```

- **Update**:
```python
article = Article.objects.first()
article.name = 'new name'
article.save()
Article.objects.filter(id=4).update(name='new name')
```

- **Delete**:
```python
article = Article.objects.first()
article.delete()
Article.objects.get(id=1).delete()
Article.objects.all().delete()
```

### Filtering
```python
Article.objects.filter(model='dyson', name__icontains='dyson')
Article.objects.filter(year__gt=2016)
Article.objects.filter(year__lt=2001)
Article.objects.get(user__username='mike')
```

### Ordering
```python
Article.objects.order_by('name')     # Ascending
Article.objects.order_by('-name')    # Descending
```

### Slicing
```python
Article.objects.all().order_by('name')[0]         # First
Article.objects.all().order_by('-name')[0]        # Last
Article.objects.all().order_by('name')[1:10]      # Limit/Offset
```

## Forms

### Basic Form
```python
from django import forms
class ArticleForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(required=False)
```

### Model Form
```python
from django.forms import ModelForm
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'description', 'price']  # Use '__all__' for all fields
```

### Rendering Forms in Template
```html
<form method="post" action="" novalidate>
    {% csrf_token %}
    {{ form }}
    <button type="submit">Submit</button>
</form>
```

### Crispy Forms (Bootstrap)
```html
{% load crispy_forms_tags %}
{{ form|crispy }}
{{ form.email|as_crispy_field }}
```

### Crispy Tailwind
```python
# settings.py
CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'

# template usage
{% load tailwind_filters %}
{{ form|crispy}}
```

### Form Validation
```python
from django.core.exceptions import ValidationError

# Field validation
def clean_first_name(self):
    data = self.cleaned_data['first_name']
    if data == 'Mike':
        raise ValidationError('Your name must not be Mike')
    return data

# Form validation
def clean(self):
    cleaned_data = super().clean()
    first_name = cleaned_data.get('first_name')
    last_name = cleaned_data.get('last_name')
    if first_name + last_name == 'MikeTaylor':
        raise ValidationError('Your name must not be Mike Taylor')
```

## Flash Messages
```python
messages.success(request, 'Login successful')
messages.error(request, 'Login error')

# Display flash in template
{% if messages %}
    {% for message in messages %}
        {{ message }}
        {{ message.tags }}
    {% endfor %}
{% endif %}
```

## User Model

### Pre-created User Model
```python
from django.contrib.auth import get_user_model
User = get_user_model()
```

### Custom User Model
```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add custom fields and methods
    pass
```
```python
# settings.py
AUTH_USER_MODEL = 'app_name.User'
```

## Authentication

### LoginView
```python
from django.contrib.auth.views import LoginView

# URL
path('login/', LoginView.as_view(), name='login')

# Template (registration/login.html)
{% extends "base.html" %}
{% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Login</button>
    </form>
{% endblock %}
```

### LogoutView
```python
from django.contrib.auth.views import LogoutView

# URL
path('logout/', LogoutView.as_view(), name='logout')

# Template Link
<a href="{% url 'logout' %}">Logout</a>
```

### SignupView
```python
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")

# URL
path('signup/', SignupView.as_view(), name='signup')

# Template (registration/signup.html)
{% extends "base.html" %}
{% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Signup</button>
    </form>
{% endblock %}
```

### Optional Pre-created Authentication Routes
```python
# urls.py
urlpatterns += path('', include('django.contrib.auth.urls'))
# /login, /logout, /signup, etc.
```

### Template Authentication Helpers
```html
<a href="{% url 'login' %}">Login</a>
<a href="{% url 'signup' %}">Signup</a>
<a href="{% url 'logout' %}">Logout</a>

{% if request.user.is_authenticated %}
    Logged in as: {{ request.user.username }}
{% endif %}
```

### Authorization

#### LoginRequiredMixin
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsCreateView(LoginRequiredMixin, generic.CreateView):
    ...
```

#### login_required
```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def search_page(request):
    ...
```

### Manual Authentication
```python
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "registration/login.html", {})

def logout_page(request):
    logout(request)
    return redirect("index")
```

### User Password Change
```python
user.set_password('raw password')
```

### Send Email
```python
# settings.py
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Send email function
from django.core.mail import send_mail

send_mail(
    subject="A new post has been created",
    message="Go to the website to see the details",
    from_email="test@test.com",
    recipient_list=["test2@test.com"]
)
```

### Signals
```python
from django.db.models.signals import post_save, pre_save

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
```

### Seeding Data
```python
from .models import Product, Category
from django.shortcuts import HttpResponse
from faker import Faker

def seed(request):
    Product.objects.all().delete()
    Category.objects.all().delete()

    categories = ["Sports", "Home"]
    for cat in categories:
        category = Category(name=cat)
        category.save()

    fake = Faker()
    for _ in range(100):
        product = Product(
            name=fake.unique.word(),
            short_description=fake.sentence(),
            main_picture=fake.image_url(),
            price=fake.random_digit() * 10,
            category=Category.objects.order_by('?').first()
        )
        product.save()

    return HttpResponse('Seeded')
```

## Environment Variables
```shell
# .env file
SECRET_KEY='your secret key'
ALLOWED_HOSTS='127.0.0.1'
```

```python
# manage.py
import dotenv

def main():
    dotenv.read_dotenv()
    ...

# settings.py
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOST