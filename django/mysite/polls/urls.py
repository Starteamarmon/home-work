from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('date/', views.date, name=''),
    path('multiplication/', views.multiplication, name='multiplication'),
    path('holidaycod/',views.holidaycod, name='holidaycod'),
]