from django.contrib import admin
from django.urls import path, include
from .views import index, add_author, add_book, get_authors, get_author_books, delete_author

urlpatterns = [
      path('', index, name="index"),
      path('add_author/', add_author, name='add_author'),
      path('add_book/', add_book, name='add_book'),
      path('authors/', get_authors, name='get_authors'),
      path('get_author_books/<int:id>/', get_author_books, name='get_author_books'),
      path('delete_author/<int:id>/', delete_author, name='delete_author'),



]
