from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("хуй")

def date(request):
    time = datetime.date.today()
    return HttpResponse(f'Текущее время: {time}')


def multiplication(request):
    a =''
    for num1 in range(1, 11):
        for num2 in range(1,11):
            a += f'{num1}*{num2} = {num1 * num2}<br>'
    return HttpResponse(a)


def holidaycod(reuest):
    today = datetime.date.today()
    NY = datetime.date(today.year, 1, 1)
    holidaycod1 = NY + datetime.timedelta(days=255)
    return HttpResponse(f'Дата дня програмиста в этом году: {holidaycod1}')