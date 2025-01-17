from django.contrib import admin

from .models import Student

# Register your models here.
@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display=('id',"name","surname")
    search_fields=('name','surname')