from django.urls import path
from . import views, old_views

app_name = 'bookshelf'
urlpatterns = [

    # class based views
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('my-books/', views.BooksView.as_view(), name='my_books'),
    path('book-detail-by-id/<str:pk>/', views.BookDetailByIdView.as_view(),
         name='book_detail_by_id'),
    path('book-detail-by-code/<str:code>/',
         views.BookDetailByCodeView.as_view(),
         name='book_detail_by_code'),
    path('book-update/<str:pk>/', views.BookUpdateView.as_view(),
         name='book_update'),
    path('book-create/', views.BookCreateView.as_view(), name='book_create'),
    path('author-create/', views.AuthorCreateView.as_view(),
         name='author_create'),

    # function based views
    path('old/welcome/', old_views.welcome, name='old_welcome'),
    path('old/my-books/', old_views.get_books_list, name='old_books_list'),
    path('old/book-detail-by-id/<str:pk>/', old_views.get_book_by_id,
         name='old_book_detail_by_id'),
    path('old/book-detail-by-code/<str:code>/', old_views.get_book_by_code,
         name='old_book_detail_by_code'),
    path('old/book-update/<str:pk>/', old_views.edit_book,
         name='old_edit_book'),
]


# class views:
# http://localhost:8000/bookshelf/welcome/
# http://localhost:8000/bookshelf/my-books/
# http://localhost:8000/bookshelf/book-detail-by-id/1/
# http://localhost:8000/bookshelf/book-detail-by-code/11/
# http://localhost:8000/bookshelf/book-update/1/
# http://localhost:8000/bookshelf/book-create/
# http://localhost:8000/bookshelf/author-create/


# function based views
# http://localhost:8000/bookshelf/old/welcome/
# http://localhost:8000/bookshelf/old/my-books/
# http://localhost:8000/bookshelf/old/book-detail-by-id/1/
# http://localhost:8000/bookshelf/old/book-detail-by-code/12/
# http://localhost:8000/bookshelf/old/book-update/1/


# https://github.com/leportella/class-based-views-example
