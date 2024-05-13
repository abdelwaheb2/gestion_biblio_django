from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField(max_length=30,null=False)
    surname = models.TextField(max_length=30,null=False)

class Book(models.Model):
    title = models.TextField(max_length=150,null=False)

class Book_Author(models.Model):
    book_id = models.ForeignKey(to=Book,on_delete=models.CASCADE)
    author_id = models.ForeignKey(to=Author,on_delete=models.CASCADE)