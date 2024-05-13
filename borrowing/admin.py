
from django.contrib import admin
from .models import Borrowing

# Register your models here.
@admin.register(Borrowing)
class Borrowing(admin.ModelAdmin):
    list_display=('id',"date_borrowing","book_returned")
    list_filter=("date_borrowing","book_returned")
    
