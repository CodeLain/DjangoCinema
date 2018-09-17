from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from CinemaCore.models import User


class CinemaHomePage(View):
    def get(self, request):
        return render(request, 'index/index.html')


class Packages(View):
    def get(self, request):
        user = User.objects.filter(fi)
        return render(request, 'index/packages.html')
