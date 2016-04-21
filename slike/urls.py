from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.pocetna, name='pocetna'),
    # url-ovi za galeriju
    url(r'^galerija/$', views.galerija, name='galerija'),
    url(r'^galerija/prva_faza/$', views.prva_faza, name='prva_faza'),

    url(r'^biografija/$', views.biografija, name='biografija'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^galerija/druga_faza/$', views.druga_faza, name='druga_faza'),
    url(r'^galerija/treca_faza/$', views.treca_faza, name='treca_faza'),
    url(r'^galerija/cetvrta_faza/$', views.cetvrta_faza, name='cetvrta_faza'),
]