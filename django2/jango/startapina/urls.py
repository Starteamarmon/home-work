from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_head, name='main'),
    path('people/', views.people, name='people'),
    path('photos/',views.photos, name='photos')
]