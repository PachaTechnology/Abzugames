# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombreDeCategoria = models.CharField("Nombre de la Categoria", max_length=50)
    descripcionDeCategoria = models.TextField(u'Descripcion de la Categoria')

    def __str__(self):
        return self.nombreDeCategoria

class Plataforma(models.Model):
    nombreDePlataforma = models.CharField("Nombre de la Plataforma", max_length=50)
    descripcionDePlataforma = models.TextField(u'Descripcion de la Plataforma')

    def __str__(self):
        return self.nombreDePlataforma  
    
class Juego(models.Model):
    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering=['-fechaDelPost']

    imagen = models.FileField(u'Caratula de Juego', upload_to='imagenesPost', blank=True)
    titulo = models.CharField(u'Título', max_length=50)
    fechaDelPost = models.DateTimeField(u'Fecha del Post', auto_now_add=True)
    contenido = models.TextField(u'Contenido')
    resumen = models.TextField(u'Resumen', default='')
    publicado = models.BooleanField(u'Publicado', default=True)
    autor = models.ForeignKey(User)
    categoria = models.ManyToManyField(u'Categoria')
    url = models.CharField(u'Link del Trailer', max_length=200)
    fechaCreacion = models.IntegerField(u'Año de Creacion')
    desarrollador = models.TextField(u'Desarrollador')
    plataforma = models.ManyToManyField(u'Plataforma')
    punt_media = models.DecimalField(u'Promedio', default=0, editable=False, max_digits=3, decimal_places=2)
    
    def __str__(self):
        return self.titulo
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture= models.FileField(u'Imagen de Perfil', upload_to='imgUser', blank=True)

    def __unicode__(self):
        return self.user.username

class Comentario(models.Model):
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Todos los Comentarios"
        ordering=['-fecha']
    asunto =  models.TextField(u'Asunto')   
    autorComen = models.ForeignKey(User)    
    mensaje = models.TextField(u'Mensaje')
    #publicado = models.BooleanField(u'Publicado?', default=True)
    fecha = models.DateTimeField(u'Fecha del Mensaje', auto_now_add=True)
    #published_in = models.ForeignKey(Juego, null=True)
    post = models.ForeignKey(Juego)
    valoracion = models.IntegerField(u'Valoración', null=True)
    
    def __str__(self):
        return self.asunto

   