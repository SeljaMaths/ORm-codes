#
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('add_author/', views.AuthorCreateView.as_view(), name='add_author'),
    path('add_book/', views.BookCreateView.as_view(), name='add_book'),
]