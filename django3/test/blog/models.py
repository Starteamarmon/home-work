from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200) #заголовок поста, строка до 200 символов.
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    
    def __str__(self):
        return f'{self.title},{self.content},{self.pub_date}'