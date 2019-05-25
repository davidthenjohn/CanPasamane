from django.shortcuts import render
from django.core.serializers import serialize
from .models import Reserva
from django.http import HttpResponse

# Create your views here.
def jsonReserves(request):
    data = serialize('json', Reserva.objects.all())
    return HttpResponse(data,content_type="application/json")