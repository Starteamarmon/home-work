from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm



def index(request):
    if request.method == 'POST':
        form = Task(request.POST)
        form.save()
        return redirect('http://127.0.0.1:8000/')
    tsk = Task.objects.all()
    form = Task()
    contex = {
        'tsk': tsk,
        'form': form
    }
    return render(request,'index.html', contex)

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('index')

    form = TaskForm()
    data = {
        'form': form
    }
    return render(request, "add.html", data)

def edit(request, id):
    hz = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        context = {'form': TaskForm(instance=hz), 'id':id}
        return render (request, 'edit.html',context)
    elif request.method == 'POST':
        form = TaskForm(request.POST, instance=hz)
        form.save()
        return redirect('index')
    

def delete(request, id):
    hz = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        context = {'form': TaskForm(instance=hz), 'id':id}
        return render (request, 'delete.html',context)
    elif request.method == 'POST':
        form = Task.objects.get(pk=id)
        form.delete()
    return redirect('index')