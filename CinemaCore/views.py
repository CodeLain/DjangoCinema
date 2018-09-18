from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from CinemaCore.forms import ActorCreationForm

from CinemaCore.models import User


class CinemaHomePage(View):
    def get(self, request):
        return render(request, 'index/index.html')


class Packages(View):
    def get(self, request):
        # user = User.objects.filter(fi)
        return render(request, 'index/packages.html')


class Forms(View):
    def get(self, request):
        form = ActorCreationForm()
        context = {
            "form": form,
        }
        return render(request, 'forms/FormsPage.html', context)

    def post(selfs, request):
        print('POSTED')
        form = ActorCreationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "form": form,
        }
        return render(request, 'forms/FormsPage.html', context)

