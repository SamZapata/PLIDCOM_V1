# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.forms.extras.widgets import *
from django.contrib.auth.models import User

class RegistrarUsuariosForm (forms.Form):

        """def __init__(self):
        super(RegistrarUsuariosForm , self).__init__()
        """
        username = forms.CharField(min_length=3,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

        usrForm_nombres = forms.CharField(max_length=100)
        usrForm_apellidos = forms.CharField(max_length=100)
        usrForm_email = forms.EmailField()
        usrForm_password = forms.CharField(min_length=6, widget=forms.PasswordInput())
        usrForm_password2 = forms.CharField(widget=forms.PasswordInput())
        usrForm_photo = forms.ImageField(required=False)

        def clean_username(self):
            #Comprueba que no exista un username igual en la db
            username = self.cleaned_data['username']
            if User.objects.filter(username=username):
                raise forms.ValidationError('Nombre de usuario ya registrado.')
            return username

        def clean_email(self):
            """Comprueba que no exista un email igual en la db"""
            usrForm_email = self.cleaned_data['usrForm_email']
            if tb_Usuario.objects.filter(usr_email=usrFormemail):
                raise forms.ValidationError('Ya existe un email igual en la db.')
            return usrForm_email

        def clean_password2(self):
            """Comprueba que password y password2 sean iguales."""
            usrForm_password = self.cleaned_data['usrForm_password']
            usrForm_password2 = self.cleaned_data['usrForm_password2']
            if usrForm_password != usrForm_password2:
                raise forms.ValidationError('Las contraseñas no coinciden.')
            return usrForm_password2