from django import forms
from LibriApp.models import Book
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

# forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'category', 'pdf_file', 'cover_image', 'is_published']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your title'}),
            'description': forms.Textarea(attrs={'class': 'form-control','cols': '40','rows': '10'})
        }