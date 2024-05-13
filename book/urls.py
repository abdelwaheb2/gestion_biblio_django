
from django.urls import path
from .views import create_author, create_book, delete_author, delete_book, edit_author, edit_book, index_author, index_book

urlpatterns = [
    path('', index_book , name='book'),
    path('new', create_book , name='new_book'),
    path('<int:id>/edit/', edit_book, name='edit_book'),
    path('<int:id>/delete/', delete_book, name='delete_book'),
    path('author/new', create_author , name='new_author'),
    path('author', index_author, name='author'),
    path('author/<int:id>/edit/', edit_author, name='edit_author'),
    path('author/<int:id>/delete/', delete_author, name='delete_author'),
]