"""
URL configuration for jango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', test.news,name='news'),
    path('history/',include('startapina.urls')),
    path('', test.tesst, name='test'),
    path('management/', test.management,name='management'),
    path('facts/', test.facts, name='facts'),
    path('cantacts/',test.cantacts,name="cantacts")
]

