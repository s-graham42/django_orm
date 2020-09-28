from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('add_a_book', views.add_a_book),
    path('add_an_author', views.add_an_author),
    path('books/<int:book_id>', views.book_page),
    path('authors/<int:author_id>', views.author_page),
    path('books/<int:book_id>/add_author_to_book/', views.add_author_to_book),
    path('authors/<int:author_id>/add_book_to_author/', views.add_book_to_author),
]