from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User

"""
Class Based Views:

https://www.dennisivy.com/post/django-class-based-views/


 we can use self.request.user in class based view to get the current logged in user


"""


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# class based view
class PostListView(ListView):
    # tell which model that view will use
    model = Post
    # tell it the template to render |
    # default -> <app>/<model>_<viewType>.html  | i.e.    blog/post_list.html
    template_name = 'blog/home.html'
    # tell the object_name of model to loop over in template  | default name = object_list
    context_object_name = 'posts'
    # "date_posted" -> loop from oldest to newest in template
    # "-date_posted" -> loop from newest to oldest  ( just add - sign)
    ordering = ['-date_posted']
    paginate_by = 5  # http://127.0.0.1:8000/?page=3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        # kwargs will be the query parameters in the url
        # get the user if it is exist or return a 404 error
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# detail view to display a single post in detail
# DetailView takes a id from the url parameter
class PostDetailView(DetailView):
    # we only need to tell the model that it will use and it will handle the rest of the functionality for us
    model = Post
    # it will look for blog/post_detail.html template by default
    # use variable named 'object' to access that specific post object


# CreateView is the view with a form
# it will share the template with the UpdateView
# Expect template name as <model>_form.html i.e post_form.html
# In this template we just display form and add submit button
# we cannot add @login_required decorator to class based views , instead we will inherit
#   LoginRequiredMixin class  that will allow us to create post only if we are logged_in
#   https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin
#   this class should be at the left most side in the inherited list
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # success_url = 'blog-home'   #  to redirect after creating post

    def form_valid(self, form):
        # we are just setting the author before the method run
        form.instance.author = self.request.user
        return super().form_valid(form)  # running parent class form_valid method


# PostUpdateView is 80% similar to PostCreateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # for checking the author who posted, can only update that post
        post = self.get_object()  # get the post object we are currently updating
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # add this attribute to redirect user to homepage

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
