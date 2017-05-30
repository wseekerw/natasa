from django.shortcuts import render
from .models import Prva_faza
from .models import Druga_faza
from .models import Treca_faza
from .models import Cetvrta_faza

# Create your views here.

def pocetna(request):
    return render(request, 'pocetna.html', {})

def galerija(request):
    return render(request, 'galerija.html', {})

def biografija(request):
    return render(request, 'biografija.html', {})

def kontakt(request):
    return render(request, 'kontakt.html', {})

def prva_faza(request):

    slike = Prva_faza.objects.all()
    return render(request, 'prva_faza.html', {'slike': slike})

def druga_faza(request):

    slike = Druga_faza.objects.all()
    return render(request, 'druga_faza.html', {'slike': slike})

def treca_faza(request):

    slike = Treca_faza.objects.all()
    return render(request, 'treca_faza.html', {'slike': slike})

def cetvrta_faza(request):

    slike = Cetvrta_faza.objects.all()
    return render(request, 'cetvrta_faza.html', {'slike': slike})
