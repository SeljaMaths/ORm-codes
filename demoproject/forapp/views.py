from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Author, Book


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'bio']
    template_name = 'add_author.html'
    success_url = '/books/'  # Redirect to the book list after successful author addition


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'add_book.html'
    success_url = '/books/'  # Redirect to the book list after successful book addition


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})