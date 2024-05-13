import datetime
from sqlite3 import Date
from django.db import models
from book.models import Book
from student.models import Student

# Create your models here.
class Borrowing(models.Model):
    student_id =models.ForeignKey(to=Student,on_delete=models.CASCADE) 
    book_id = models.ForeignKey(to=Book,on_delete=models.CASCADE)
    date_borrowing =models.DateTimeField(null=False)
    book_returned = models.BooleanField(null=False,default=False)