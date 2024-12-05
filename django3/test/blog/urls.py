from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tt/', include('test.urls')),
    path('',views.index, name='index')
]
