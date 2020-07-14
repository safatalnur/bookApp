from django import forms
from . import models

class CreateBook(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'illustrated', 'age', 'bookImage']