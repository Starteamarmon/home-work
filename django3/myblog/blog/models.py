from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField('Data published:')

    def __str__(self):
        return f'{self.title}, {self.content} {self.published_date}'
