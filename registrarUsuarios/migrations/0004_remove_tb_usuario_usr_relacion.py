# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-14 16:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrarUsuarios', '0003_tb_usuario_usr_relacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tb_usuario',
            name='usr_relacion',
        ),
    ]
