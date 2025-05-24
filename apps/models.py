from django.db import models

class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=[('femenino', 'Femenino'), ('kids', 'Kids'), ('unica', 'Única')], default='femenino')
    equipo = models.CharField(max_length=100, null=True, blank=True)
    torneo = models.DateField(null=True, blank=True)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    equipo_fecha = models.ForeignKey(MiModelo, on_delete=models.CASCADE, related_name='jugadores')
    posicion = models.CharField(max_length=50, null=True, blank=True)  # Optional: player position