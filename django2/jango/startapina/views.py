from django.shortcuts import render
from django.http import HttpResponse

def main_head(reuqest):
    return HttpResponse('<h4>История<h4/><br><a href="http://127.0.0.1:8000/history/people">Известные пеопле города</a><br><a href="http://127.0.0.1:8000/history/photos">фото известных Пеопле</a><br><a href="http://127.0.0.1:8000/">на главную</a>')


def people(request):
    return HttpResponse('Известные пеопле города<br><br><a href="http://127.0.0.1:8000/history">назад</a><br><a href="http://127.0.0.1:8000/">на главную</a>')

def photos(request):
    return HttpResponse('<H1>фото известных Пеопле<h1/><br><img src="https://sun9-19.userapi.com/s/v1/ig2/wHR84igTCrd-B_IC7ZfwVrzq1pmxUyew3JQ3SZlcuIrAfpfLjciGV1h3DnDnRsa_QK6UqMzelIchJU7KD948uRz1.jpg?quality=95&blur=50,20&as=32x22,48x33,72x50,108x75,160x111,240x166,360x249,480x332,540x373,640x443,720x498,1080x747&from=bu&u=gN_FMYV1UaTzUbCF8wfWF4faZ0etUmBD2bjaIir1yUE&cs=807x558"><br><a href="http://127.0.0.1:8000/history">назад</a><br><a href="http://127.0.0.1:8000/">на главную</a>')