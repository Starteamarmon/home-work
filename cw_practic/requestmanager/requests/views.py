from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Request
from . forms import ReqestForm

def create_request(request):
    if request.method == 'POST':
        form = ReqestForm(request.POST)
        form.save()
        return redirect('request_list')

def request_list(request):
    rqs = Request.objects.all()
    return render(request,'list.html', {'rqs': rqs})