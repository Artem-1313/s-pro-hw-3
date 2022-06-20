from .models import Author, Book
from django import forms


class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['f_name', 'l_name']
        labels = {
            'f_name': "First Name",
            'l_name': "Surname"
        }

class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'