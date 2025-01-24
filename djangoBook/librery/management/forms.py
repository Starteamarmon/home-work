from .models import Book,User,Rental
from django.forms import ModelForm, DateTimeInput, Select, TextInput, Textarea, NumberInput
# from django import forms


# class SignupForm(forms.ModelForm):
  # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
  #   'class': 'form-control',
  #   'id': 'floatingPasswordConfirm',
  #   'placeholder': 'Подтверждение пароля',
  #   'required': True
  # }))

  # class Meta:
  #   model = User
  #   fields = ['firstname', 'lastname', 'username', 'email', 'password']

  #   widgets = {
  #     'firstname': forms.TextInput(attrs={
  #       'class': 'form-control',
  #       'id': 'floatingTitle',
  #       'placeholder': 'Очень простая задача',
  #       'required': True
  #     }),
  #     'lastname': forms.TextInput(attrs={
  #       'class': 'form-control',
  #       'id': 'floatingLastname',
  #       'aria-label': 'Фамилия',
  #       'placeholder': 'Очень простая задача',
  #       'required': True
  #     }),
  #     'username': forms.TextInput(attrs={
  #       'class': 'form-control',
  #       'id': 'floatingUsername',
  #       'placeholder': 'Логин пользователя',
  #       'aria-label': 'Логин пользователя',
  #       'required': True
  #     }),
  #     'email': forms.EmailInput(attrs={
  #       'class': 'form-control',
  #       'id': 'floatingEmail',
  #       'placeholder': 'Почта',
  #       'required': True
  #     }),
  #     'password': forms.PasswordInput(attrs={
  #       'class': 'form-control',
  #       'id': 'floatingPassword',
  #       'placeholder': 'Пароль',
  #       'required': True
  #     }),
  #   }

  # def clean(self):
  #   cleaned_data = super().clean()
  #   password = cleaned_data.get('password')
  #   confirm_password = cleaned_data.get('confirm_password')
  #   if password != confirm_password:
  #     raise forms.ValidationError('Пароли не совпадают!')
  #   return cleaned_data

# class RegisterForm(forms.ModelForm):
#   password = forms.CharField(widget=forms.PasswordInput)
#   confirm_password = forms.CharField(widget=forms.PasswordInput)
    
#   class Meta:
#     model = User
#     fields = ['username', 'email', 'password']
  
#   def clean(self):
#     cleaned_data = super().clean()
#     password = cleaned_data.get('password')
#     confirm_password = cleaned_data.get('confirm_password')
#     if password != confirm_password:
#       raise forms.ValidationError("Пароли не совпадают!")
#     return cleaned_data


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