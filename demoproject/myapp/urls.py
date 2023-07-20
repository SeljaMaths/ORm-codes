
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_list, name='book_list'),
    path('author_add/', views.add_author, name='add_author'),
    path('book_add/', views.add_book, name='add_book'),
]