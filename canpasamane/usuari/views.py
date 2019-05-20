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

def historia(request):
    return render(request, 'historia.html', {})

def activitats(request):
    return render(request, 'Activitats.html', {})

def contacte(request):
    return render(request, 'contacte.html', {})

def reserves(request):
    return render(request, 'reserves.html', {})
#home
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
            print(profile.telefon)
            print(profile.user.id)
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
            message = "nope"
            return render(request, 'login.html')
    else:
        return render(request, 'login.html', {})