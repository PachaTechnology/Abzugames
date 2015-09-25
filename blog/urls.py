from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$','blog.views.home', name='home'),
                       url(r'^Login/$','blog.views.login', name='login'),
                       url(r'^Registro/$','blog.views.registro', name='registro'),
                      )