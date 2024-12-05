from django.db import models
from django.forms.widgets import CheckboxSelectMultiple



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.is_completed}'
    
