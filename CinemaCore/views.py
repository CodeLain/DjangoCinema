from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from CinemaCore.forms import ActorCreationForm

from CinemaCore.models import User


class CinemaHomePage(View):
    def get(self, request):
        user = request.user
        print(user.is_authenticated)
        if user.is_authenticated:
            request.session['fav_color'] = 'blue'
            print('something')
            print(user.first_name)
            print('is clinet? %s' % user.is_client)
            print('is employee? %s' % user.is_employee)
        context = {
            'user': user
        }
        return render(request, 'index/index.html', context)

    def post(self, request):
        #NEED TO FIX THE AUTHENTIFICATION, IS RETURNING FALSE ON BOTH OF THE USER TYPES
        #PROBABLY
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        login(request, user)
        print(user.first_name)
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
        form = ActorCreationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {
            "form": form,
        }
        return render(request, 'forms/FormsPage.html', context)


class ActivateUser(View):
    def get(self, request, token):
        user = User.objects.get(activation_id=token)
        user.is_active = True
        user.save()
        return HttpResponse('user activated')


