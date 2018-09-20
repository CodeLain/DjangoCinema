"""Cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from CinemaCore.views import CinemaHomePage, Packages, Forms, ActivateUser

urlpatterns = [
    path('', CinemaHomePage.as_view(), name='index'),
    path('packages/', Packages.as_view(), name='packages'),
    path('create_actor/', Forms.as_view(), name='create_actor'),
    path('articles/<uuid:token>/', ActivateUser.as_view()),
]
