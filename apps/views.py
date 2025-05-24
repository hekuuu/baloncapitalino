from django.shortcuts import render
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset


from django.shortcuts import render
from .models import Jugador

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
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset


from django.shortcuts import render
from .models import Jugador

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
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset


from django.shortcuts import render
from .models import Jugador

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
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)
        if torneo:
            queryset = queryset.filter(equipo_fecha__torneo=torneo)
        return queryset
from .models import MiModelo
from rest_framework import generics
from .models import Jugador, MiModelo
from .serializers import JugadorSerializer

def baloncapitalino_view(request):
    return render(request, "baloncapitalino.html")

def femenino_view(request):
    equipos = MiModelo.objects.filter(categoria='femenino')
    return render(request, 'femenino.html', {'equipos': equipos})
def kids_view(request):
    equipos = MiModelo.objects.filter(categoria='kids')
    return render(request, 'kids.html', {'equipos': equipos})
def unica_view(request):
    equipos = MiModelo.objects.filter(categoria='unica')
    return render(request, 'unica.html', {'equipos': equipos})
def kids_view(request):
    return render(request, 'kids.html')

class JugadorListAPIView(generics.ListAPIView):
    serializer_class = JugadorSerializer

    def get_queryset(self):
        queryset = Jugador.objects.all()
        equipo = self.request.query_params.get('equipo')
        torneo = self.request.query_params.get('torneo')
        if equipo:
            queryset = queryset.filter(equipo_fecha__equipo__icontains=equipo)