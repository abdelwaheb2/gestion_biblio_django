from django.urls import path

from .views import create, delete, edit, index



urlpatterns = [
    path('new', create , name='new_borrowing'),
    path('', index, name='borrowing'),
    path('<int:id>/edit', edit, name='edit_borrowing'),
    path('<int:id>/delete', delete, name='delete_borrowing'),
]