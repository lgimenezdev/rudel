# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-09 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gaseosa',
            fields=[
                ('id_gaseosa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('marca', models.CharField(max_length=10, verbose_name='Marca')),
                ('presentacion', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=20)),
            ],
        ),
    ]
