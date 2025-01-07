from .models import Book,User,Rental
from django.forms import ModelForm, DateTimeInput, Select, TextInput, Textarea, NumberInput

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year' , 'genre' , 'is_available']

        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Название Книги'
            }),
            "author": TextInput(attrs={
                'placeholder': 'Автор'
            }),
            "published_year": NumberInput(attrs={
                'placeholder': 'год'
            }),
            "genre": Textarea(attrs={
                'placeholder': 'Жанр'
            }),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = ['user', 'book', 'rental_date', 'return_date']

        widgets = {
            'user': Select(attrs={
                'placeholder' : 'пользователь'
            }),
            'book': Select(attrs={
                'paceholder' : 'Книга'
            }),
            'rental_date': DateTimeInput(attrs={
                'placeholder' : 'дата аренды'
            }),
            'return_date': DateTimeInput(attrs={
                'placeholder' : 'дата возврата'
            })
        }