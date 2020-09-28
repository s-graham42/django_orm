from django.shortcuts import render, HttpResponse, redirect
from books_authors_app.models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def books(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, "books.html", context)

def add_a_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return redirect("/books")

def authors(request):
    context = {
        "all_authors": Author.objects.all(),
    }
    return render(request, "authors.html", context)

def add_an_author(request):
    Author.objects.create(first_name=request.POST['firstName'], last_name=request.POST['lastName'], notes=request.POST['notes'])
    return redirect("/authors")

def book_page(request, book_id):
    context = {
        'this_book': Book.objects.get(id=book_id),
        'all_authors': Author.objects.all(),
    }
    return render(request, 'book_page.html', context)

def author_page(request, author_id):
    context = {
        'this_author': Author.objects.get(id=author_id),
        'all_books': Book.objects.all(),
    }
    return render(request, 'author_page.html', context)

def add_author_to_book(request, book_id):
    book_to_get_author = Book.objects.get(id=book_id)
    author_to_add = Author.objects.get(id=request.POST['add_this_author'])
    book_to_get_author.authors.add(author_to_add)
    return redirect("/books/" + str(book_id))

def add_book_to_author(request, author_id):
    author_to_get_book = Author.objects.get(id=author_id)
    book_to_add = Book.objects.get(id=request.POST['add_this_book'])
    author_to_get_book.books.add(book_to_add)
    return redirect("/authors/" + str(author_id))