from django.urls import path

from student.views import create, delete, edit, index



urlpatterns = [
    path('new', create , name='new_student'),
    path('', index, name='student'),
    path('<int:id>/edit', edit, name='edit_student'),
    path('<int:id>/delete', delete, name='delete_student'),
]