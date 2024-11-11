from django.http import HttpResponse

def tesst(request):
    return HttpResponse('<h3>ГЛавная страница<h3/><br><a href="http://127.0.0.1:8000/management/">руководство города</a><br><a href="http://127.0.0.1:8000/facts/">Факты о городе</a><br><a href="http://127.0.0.1:8000/cantacts/">Контактные телефоны городских служб.</a><br><a href="http://127.0.0.1:8000/news/">Новости</a><br><a href="http://127.0.0.1:8000/history/">История</a>')

def management(request):
    return HttpResponse('<h5>руководство города<h5/><br><a href="http://127.0.0.1:8000/">на главную</a>')

def facts(request):
    return HttpResponse('Факты о городе<br><a href="http://127.0.0.1:8000/">на главную</a>')

def cantacts(request):
    return HttpResponse('Контактные телефоны городских служб.<br><a href="http://127.0.0.1:8000/">на главную</a>')

def news(request):
    return HttpResponse('НОВОСТИ<br><a href="http://127.0.0.1:8000/">на главную</a>')