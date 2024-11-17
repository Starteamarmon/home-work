from django.shortcuts import render
from django.http import HttpResponse

def head(request):
    return HttpResponse('Главная')

def news(request):
    return HttpResponse('Новости города')

def management(request):
    return HttpResponse('Руководство города')

def satis_faction(request):
    return HttpResponse('Факты о городе')

def contact(request):
    return HttpResponse('Контактные телефоны городских служб')

