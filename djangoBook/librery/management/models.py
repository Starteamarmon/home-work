from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class User(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.username}'


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    rental_date = models.DateTimeField(auto_created=True)
    return_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.user}"