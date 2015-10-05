from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
urlpatterns = patterns('',
                      url(r'^home/$','blog.views.home', name='home'),
                       url(r'^$', 'blog.views.main', name='main'),
                       url(r'^signup$', 'blog.views.signup', name='signup'),
                       url(r'^login$', login, {'template_name': 'loguin.html', }, name="login"),
                       url(r'^logout$', logout, {'template_name': 'loguin.html', }, name="logout"),
                      )