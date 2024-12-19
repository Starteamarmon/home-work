from .models import Book,User,Rental
from django.forms import ModelForm, TextInput, DateInput, Select

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year' , 'genre' , 'is_available']

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
            'rental_date': DateInput(attrs={
                'placeholder' : 'дата аренды'
            }),
            'return_date': DateInput(attrs={
                'placeholder' : 'дата возврата'
            })
        }