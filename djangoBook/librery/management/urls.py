from django.urls import path
from . import views

urlpatterns = [
    path('',views.book,name='book'),
    path('search/',views.search,name='search'),
    path('genre/<str:genre>',views.genre,name='genre'),
    path('users', views.users, name='users'),
    path('books_in_users/<str:username>', views.books_in_users, name='books_in_users'),
    path('free_list', views.free_list, name='free_list'),
    path('rent/<int:id>/',views.rent, name='rent')
]