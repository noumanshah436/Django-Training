from django.views.generic import (
    CreateView, DetailView, ListView,
    TemplateView, UpdateView,
    # DeleteView
)
from django.urls import reverse_lazy

from .forms import AuthorForm, BookForm
from .models import Author, Book


class WelcomeView(TemplateView):
    template_name = 'welcome.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'my-author-create.html'
    form_class = AuthorForm
    success_url = reverse_lazy('bookshelf:my_books')


class BooksView(ListView):
    model = Book
    template_name = 'my-books.html'
    # by default it will look for -> bookshelf/book_list.html


class BookDetailByIdView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'
    # by default it will look for -> bookshelf/book_detail.html


class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'

    def get_object(self):
        return Book.objects.get(code=self.kwargs['code'])


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'my-book-edit.html'
    # by default it will look for -> bookshelf/book_form.html
    form_class = BookForm
    success_url = reverse_lazy('bookshelf:my_books')


class BookCreateView(CreateView):
    model = Book
    template_name = 'my-book-create.html'
    # by default it will look for ->  bookshelf/book_form.html
    form_class = BookForm
    success_url = reverse_lazy('bookshelf:my_books')


# class BookDeleteView(DeleteView):
#     model = Book
#     # here we can specify the URL
#     # to redirect after successful deletion
#     success_url = reverse_lazy('bookshelf:my_books')
