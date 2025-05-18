from django.db import models

class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()