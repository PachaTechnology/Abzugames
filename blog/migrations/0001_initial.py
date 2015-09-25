# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre de la Categoria')),
                ('descripcion', models.TextField(verbose_name='Descripcion de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=50, verbose_name=b'publicado por:')),
                ('contenido', models.TextField(max_length=500, verbose_name=b'Comentario')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha')),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('resumen', models.CharField(max_length=512, verbose_name='Resumen')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado?')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ManyToManyField(to='blog.Categoria')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Mi Entrada',
                'verbose_name_plural': 'Todas mis entradas',
            },
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.FileField(default=b'null', upload_to=b'imagendeljuego', verbose_name='Caratula de Juego')),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('resumen', models.CharField(max_length=512, verbose_name='Resumen')),
                ('critica', models.TextField(verbose_name='Critica')),
                ('publicado', models.BooleanField(default=True, verbose_name='Publicado')),
                ('puntajeSegunAutor', models.IntegerField(verbose_name='Puntaje por el autor')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='blog.Categoria')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Juego',
                'verbose_name_plural': 'Juegos',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(to='blog.Entrada'),
        ),
    ]
