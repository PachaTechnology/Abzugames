# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField("Nombre de la Categoria", max_length=50)
    descripcion = models.TextField(u'Descripcion de la categoria')

    def __str__(self):
        return self.nombre

    
class Juego(models.Model):
    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering=['-fechaDelPost']

    imagen = models.FileField(u'Caratula de Juego', upload_to='imagendeljuego', default='null')
    titulo = models.CharField(u'Título', max_length=50)
    fechaDelPost = models.DateTimeField(u'Fecha del Post', auto_now_add=True)
    contenido = models.TextField(u'Contenido')
    publicado = models.BooleanField(u'Publicado', default=True)
    autor = models.ForeignKey(User)
    categoria = models.ManyToManyField(Categoria)
    url = models.CharField(u'Link del Trailer', max_length=200)
    fechaCreacion = models.IntegerField(u'Año de Creacion')
    desarrollador = models.TextField(u'Desarrollador')    
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    class Meta:
        ordering=['fecha']
    post = models.ForeignKey(Juego)
    nick = models.CharField('publicado por:', max_length=50)
    contenido = models.TextField('Comentario', max_length=500)
    fecha = models.DateTimeField('Fecha', auto_now_add=True)
    puntajeSegunComunidad = models.IntegerField(u'puntajeSegunComunidad')    
        
    def __str__(self):
        return self.nick, self.puntajeSegunComunidad
