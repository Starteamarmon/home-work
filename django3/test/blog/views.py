from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    question = Post.objects.get(pk=id)
    return render(request, 'index.html')
