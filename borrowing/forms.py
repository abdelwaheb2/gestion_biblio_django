from .models import Borrowing
from django import forms

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['date_borrowing','book_returned' ]
        widgets = {
            'date_borrowing': forms.DateTimeInput(attrs={'class': 'form-control' , 'type' :'datetime-local' }), 
            'book_returned': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
        }
