from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    title = models.CharField(max_length=100,verbose_name='Книга')
    author = models.CharField(max_length=100,verbose_name='Автор')
    published_year = models.IntegerField(verbose_name='Год публигации')
    genre = models.CharField(max_length=100,verbose_name='Жанр')
    is_available = models.BooleanField(default=True,verbose_name='Аренда')

    def __str__(self):
        return f'{self.title}'


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    username = models.CharField(max_length=10, unique=True,verbose_name='Юзер')
    email = models.EmailField(verbose_name='Почта')

    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'


class Rental(models.Model):
    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='Пользователь')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING,verbose_name='Книга')
    rental_date = models.DateTimeField(verbose_name='Начало аренды')
    return_date = models.DateTimeField(verbose_name='Дата возврата')

    def __str__(self):
        return f"{self.user}"