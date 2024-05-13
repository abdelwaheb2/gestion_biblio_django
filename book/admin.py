from django.contrib import admin
from .models import Book,Author, Book_Author

# Register your models here.
@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display=('id',"title")
    search_fields=('title',)

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display=('id',"name","surname")
    search_fields=('name','surname')
admin.site.register(Book_Author)