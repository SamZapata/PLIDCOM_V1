# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.primera_vista, name='primera_vista'),
    url(r'^nuevoHabitante_registro/$', views.nuevoHabitante_registro,
    name='nuevoHabitante_registro'),
    url(r'^nuevoHabitante/(?P<user_id>[0-9]+)/$', views.nuevo_habitante,
    name='nuevoHabitante'),
    url(r'^nuevoHabitante_registro/confirmado$', views.nuevoHabitante_registro,
    name='nuevoHabitante_registro/confirmado'),
]
