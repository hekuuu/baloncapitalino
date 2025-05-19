from django.shortcuts import render
from .models import MiModelo

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.all()
    return render(request, 'femenino.html', {'equipos': equipos})
def unica_view(request):
    return render(request, 'unica.html')
def kids_view(request):
    return render(request, 'kids.html')