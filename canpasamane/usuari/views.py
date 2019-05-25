from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.serializers import serialize
from reserva.models import Reserva
import json

from .form import ExtendedUserCreationForm, UserProfileForm
from .models import Usuari
# Create your views here.

#Bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html', {})

def historia(request):
    return render(request, 'historia.html', {})

def activitats(request):
    return render(request, 'Activitats.html', {})

def contacte(request):
    return render(request, 'contacte.html', {})

def reserves(request):
    llistaReserves = Reserva.objects.all()
    llista = [ serializer(x) for x in llistaReserves]
    
    context = {'var':llista}
    return render(request, 'reserves.html', context)
#home
def serializer(reserva):
    dies = ""
    for x in reserva.data_reserva:
        dies += str(x)+" "
    return dies

def home(request):
    return render(request, 'home.html')


#Registrar usuario
def registro(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()


            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.usuari_id = profile.user.id
            profile.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
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
                return redirect('usuario:bienvenida')
            else:
                return render(request, 'login.html')
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(username, password))
            messages.add_message(request, messages.INFO, 'Mail o contrasenya incorrecte')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html', {})