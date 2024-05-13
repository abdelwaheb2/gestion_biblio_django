from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.TextField(max_length=30,null=False)
    surname = models.TextField(max_length=30,null=False)