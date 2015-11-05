from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
urlpatterns = patterns('',

                       url(r'^home$','blog.views.home', name='home'),
                        url(r'^$', 'blog.views.home', name='home'),
                      # url(r'^$', 'blog.views.main', name='main'),
                       url(r'^explorar-post$', 'blog.views.explorarpost', name='explorar-post'),
                       url(r'^signup$', 'blog.views.signup', name='signup'),
                       url(r'^login$', login, {'template_name': 'loguin.html', }, name="login"),
                       url(r'^logout$', logout, {'template_name': 'loguin.html', }, name="logout"),
                       url(r'^crear-post$', 'blog.views.crear_juego', name='crear_juego'),
                        url(r'^ver-juego/(?P<id_post>[0-9]+)/$', 'blog.views.verjuego', name='ver_juego'),
                       url(r'^perfil$', 'blog.views.perfil', name='perfil'),
                      )
