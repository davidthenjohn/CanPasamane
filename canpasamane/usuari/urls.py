from django.urls import path, include
from . import views
from reserva.views import jsonReserves

app_name = 'usuario'

urlpatterns = [
    path('', views.bienvenida, name="bienvenida"),
    path('registro/', views.registro, name="api"),
    path(r'accounts/login', views.inicioSesion, name='inicioSesion'),
    path('home/', views.bienvenida, name="home"),
    path('registro', views.registro, name="registro"),
    path('activitats/', views.activitats, name="activitats"),
    path('contacte/', views.contacte, name="contacte"),
    path('reserva/', views.reserves, name="reserva"),
]
