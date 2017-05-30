from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Prva_faza(models.Model):
    slike1 = models.ImageField("prva_faza_slike", upload_to="images/prva_faza/")
    ime_slike1 = models.CharField(max_length=50)
    dimenzije1 = models.CharField(max_length=50)
    tehnika1 = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ime_slike1

class Druga_faza(models.Model):
    slike2 = models.ImageField("druga_faza_slike", upload_to="images/druga_faza/")
    ime_slike2 = models.CharField(max_length=50)
    dimenzije2 = models.CharField(max_length=50)
    tehnika2 = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ime_slike2

class Treca_faza(models.Model):
    slike3 = models.ImageField("treca_faza_slike", upload_to="images/treca_faza/")
    ime_slike3 = models.CharField(max_length=50)
    dimenzije3 = models.CharField(max_length=50)
    tehnika3 = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ime_slike3

class Cetvrta_faza(models.Model):
    slike4 = models.ImageField("cetvrta_faza_slike", upload_to="images/cetvrta_faza/")
    ime_slike4 = models.CharField(max_length=50)
    dimenzije4 = models.CharField(max_length=50)
    tehnika4 = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ime_slike4