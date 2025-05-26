import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import MiModelo, Jugador
from .serializers import JugadorSerializer
from .models import Noticia

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})

def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})

def home(request):
    return render(request, 'baloncapitalino.html')
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})

def busqueda_jugadores(request):
    equipo = request.GET.get('equipo', '')
    torneo = request.GET.get('torneo', '')
    jugadores = None
    if equipo or torneo:
        jugadores = Jugador.objects.all()
        if equipo:
            jugadores = jugadores.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            jugadores = jugadores.filter(equipo_fecha__torneo=torneo)
    return render(request, 'busqueda.html', {'jugadores': jugadores})

from rest_framework import generics
from .models import Jugador
from .serializers import JugadorSerializer

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer
    def get_queryset(self):
        equipo = self.request.GET.get('equipo', '')
        torneo = self.request.GET.get('torneo', '')
        queryset = Jugador.objects.all()
        if equipo:
            queryset = queryset.filter(equipo__nombre__icontains=equipo)
        if torneo:
            queryset = queryset.filter(torneo__nombre__icontains=torneo)
        return queryset

def scrape_jugadores(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Solo se permiten peticiones GET'}, status=400)
    url = 'https://www.microfutbol.co'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    noticias = []
    for div in soup.select('.inner-block'):
        titulo = div.select_one('h2 a')
        if titulo:
            titulo_text = titulo.get_text(strip=True)
            noticia_obj, created = Noticia.objects.get_or_create(titulo=titulo_text)
            noticias.append({'titulo': titulo_text, 'created': created})
    return JsonResponse({'noticias': noticias})
