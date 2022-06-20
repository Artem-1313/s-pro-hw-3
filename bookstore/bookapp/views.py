from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from .forms import AddAuthor, AddBook


def index(request):

    if request.method == "GET" and (request.GET.get('search') is not None):
        search = request.GET.get('search')
        books = Book.objects.filter(title__contains=search)
    else:
        books = Book.objects.all()
    return render(request, 'bookapp/index.html', context={"books": books})


def add_author(request):

    if request.method == 'POST':
        form = AddAuthor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddAuthor()
    return render(request, "bookapp/add_author.html", context={"form": form})



def add_book(request):
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddBook()
    return render(request, "bookapp/add_book.html", context={"form": form})


def get_authors(request):
    authors = Author.objects.all()
    return render(request, "bookapp/get_authors.html", context={"authors": authors})


def get_author_books(request, id):
    author=get_object_or_404(Author, id=id)
    author_books = author.book_set.all()
    return render(request, "bookapp/get_author_books.html", context={"author_books": author_books, "author": author})


def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return redirect('get_authors')


