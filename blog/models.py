# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
global puntaje      

class Juego(models.Model):
    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering=['-fecha']

    imagen = models.FileField(u'Caratula de Juego', upload_to='imagendeljuego', default='null')
    titulo = models.CharField(u'Título', max_length=100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    critica = models.TextField(uCritica')
    publicado = models.BooleanField(u'Publicado', default=True)
    autor = models.ForeignKey(User)
    tag = models.ManyToManyField('Categoria')
    puntajeSegunAutor = models.IntegerField(u'Puntaje por el autor')
    
    def __str__(self):
        return self.titulo

    
class Categoria(models.Model):
    nombre = models.CharField("Nombre de la Categoria", max_length=50)
    descripcion = models.TextField(u'Descripcion de la categoria')

    def __str__(self):
        return self.nombre
    

class Comentario(models.Model):
    class Meta:
        ordering=['fecha']
    post = models.ForeignKey(Entrada)
    nick = models.CharField("publicado por:", max_length=50)
    puntaje = models.IntegerField(u"Calificacion", max_value=5, min_value=1)
    contenido = models.TextField("Comentario", max_length=500)
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
    
        
    def __str__(self):
        return self.nick, self.puntaje
