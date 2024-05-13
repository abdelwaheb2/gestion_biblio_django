# forms.py
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'username','password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.TextInput(attrs={'class': 'form-control mb-5'}), 
            'username': forms.TextInput(attrs={'class': 'form-control'}), 
            'password': forms.TextInput(attrs={'class': 'form-control' , 'type':'password'}),
        }
        help_texts = {
            'username': None
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if user.password :
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
