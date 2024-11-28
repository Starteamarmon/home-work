from .models import Task
from django.forms import ModelForm, TextInput, CheckboxInput




class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','is_completed']

        widgets = {
            'title': TextInput(attrs={
                'placeholder' : 'Задача'
            }),
            'description': TextInput(attrs={
                'placeholder' : 'Описание'
            }),
            'is_completed': CheckboxInput(attrs={
                'class': 'required checkbox form-control'
            })

            #     'created_at': DateTimeInput(attrs={
            #     'placeholder' : 'Статус'
            # })
        }