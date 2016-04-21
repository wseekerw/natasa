# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cetvrta_faza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slike4', models.ImageField(upload_to='images/cetvrta_faza/', verbose_name='cetvrta_faza_slike')),
                ('ime_slike4', models.CharField(max_length=50)),
                ('dimenzije4', models.CharField(max_length=50)),
                ('tehnika4', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Druga_faza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slike2', models.ImageField(upload_to='images/druga_faza/', verbose_name='druga_faza_slike')),
                ('ime_slike2', models.CharField(max_length=50)),
                ('dimenzije2', models.CharField(max_length=50)),
                ('tehnika2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prva_faza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slike1', models.ImageField(upload_to='images/prva_faza/', verbose_name='prva_faza_slike')),
                ('ime_slike1', models.CharField(max_length=50)),
                ('dimenzije1', models.CharField(max_length=50)),
                ('tehnika1', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Treca_faza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slike3', models.ImageField(upload_to='images/treca_faza/', verbose_name='treca_faza_slike')),
                ('ime_slike3', models.CharField(max_length=50)),
                ('dimenzije3', models.CharField(max_length=50)),
                ('tehnika3', models.CharField(max_length=50)),
            ],
        ),
    ]