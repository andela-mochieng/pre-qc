# from django import forms
from django.forms import ModelForm, TextInput, Select
from .models import Category, Book


class createCategoryForm(ModelForm):

    class Meta(ModelForm):
        model = Category
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class createBookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'category']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'})
        }
