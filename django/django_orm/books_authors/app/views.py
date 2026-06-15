from app.models import Book, Author
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def books(request):
    if request.method == 'POST':
        book = Book.objects.create(title=request.POST['title'], description=request.POST['description'])
        return redirect('books')
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    authors = Author.objects.all()
    return render(request, 'book_details.html', {'book': book, 'authors': authors})

def add_author(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}/')

def authors(request):
    if request.method == 'POST':
        author = Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        return redirect('authors')
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    books = Book.objects.all()
    return render(request, 'author_details.html', {'author': author, 'books': books})

def add_book(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect('author_detail', author_id=author_id)
