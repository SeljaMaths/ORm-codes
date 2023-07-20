# myapp/views.py

from django.shortcuts import render, redirect
from .models import Author, Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'for/book_list.html', {'books': books})

def add_author(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        if name and bio:
            author = Author.objects.create(name=name, bio=bio)
            return redirect('book_list')
    return render(request, 'for/add_author.html')

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        if title and author_id and publication_date:
            book = Book.objects.create(
                title=title,
                author_id=author_id,
                publication_date=publication_date
            )
            return redirect('book_list')
    return render(request, 'for/add_book.html')
