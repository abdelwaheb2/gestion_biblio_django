from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), 
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','surname']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'surname': forms.TextInput(attrs={'class': 'form-control'}), 
        }