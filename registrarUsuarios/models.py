#from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Modelo para Registrar un usuario

class tb_Usuario(models.Model):

    id_usuario = models.AutoField(primary_key=True)
    usr_usuario = models.CharField(max_length=50, unique=True)
    usr_nombres = models.CharField(max_length=100)
    usr_apellidos = models.CharField(max_length=100)
    usr_email = models.EmailField()
    usr_password = models.CharField(max_length=20)
    usr_photo = models.ImageField(upload_to='photos/')
    #usr_relacion = models.OneToOneField(settings.AUTH_USER_MODEL)

    #para modificar la vista en el admin django
    class Admin:
        list_display = ('usr_usuario', 'usr_apellidos', 'usr_nombres')
        list_filter = ('usr_usuario')
        ordering = ('usr_apellidos',)
        search_fields = ('usr_email',)


    #para ordenar la salida de datos
    #class Meta:
        #ordering = ['usr_apellidos']

    def __str__(self):
        return self.usr_usuario


class tb_Pais(models.Model):

    id_pais = models.AutoField(primary_key=True)
    pais_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.pais_nombre


class tb_Departamento(models.Model):

    id_departamento = models.AutoField(primary_key=True)
    dep_nombre = models.CharField(max_length=100)
    pais_id_departamento = models.ForeignKey(tb_Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.dep_nombre

class tb_Municipio(models.Model):

    id_municipio = models.AutoField(primary_key=True)
    mun_nombre = models.CharField(max_length=100)
    dep_id_municipio = models.ForeignKey(tb_Departamento,
                        on_delete=models.CASCADE)

    def __str__(self):
        return self.mun_nombre