from .models import Request
from django.forms import ModelForm, TextInput, Textarea

class ReqestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['name','email','message']

        widgets = {
            'name': TextInput(attrs={
                'placeholder' : 'Имя'
            }),
            'email': TextInput(attrs={
                'placeholder' : 'Почта'
            }),
            'message': Textarea(attrs={
                'placeholder' : 'СОобщение'
            })
        }