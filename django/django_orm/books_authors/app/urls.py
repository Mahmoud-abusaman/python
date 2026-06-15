
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/authors/', views.add_author, name='add_author'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/<int:author_id>/books/', views.add_book, name='add_book'),
]