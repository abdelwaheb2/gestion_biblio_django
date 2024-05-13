from student.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','surname']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'surname': forms.TextInput(attrs={'class': 'form-control'}), 
        }
