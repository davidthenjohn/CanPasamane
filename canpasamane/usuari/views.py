from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import ExtendedUserCreationForm, UserProfileForm
from .models import Usuari
# Create your views here.

#Bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html', {})


#home
def home(request):
    return render(request, 'home.html')


#Registrar usuario
def registro(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            usuario = form.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            usuari = authenticate(username=username, password=password)
            login(request, usuari)

            return redirect('usuario:home')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}

    return render(request, 'registro.html', context)


#Iniciar sesion
def inicioSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('usuario:home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})