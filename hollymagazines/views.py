from django.shortcuts import render
from datetime import date

# Create your views here.
from django.http import HttpResponse

from . models import Publicatie, Revista
from django.urls import resolve


def lista_reviste(request):
    publicatie = Publicatie.objects.all()
    revista = Revista.objects.all()

    return render(
        request, template_name='lista_reviste.html',
        context={'publicatii': publicatie, 'reviste': revista})

def lista_reviste_pub(request, pub_name):
    publicatii = Publicatie.objects.all()

    publicatie = Publicatie.objects.get(name=pub_name)
    reviste = Revista.objects.filter(publicatie=publicatie)

    return render(
        request, template_name='lista_reviste.html',
        context={'publicatii': publicatii, 'reviste': reviste}
    )

def detalii_revista(request, slug):
    revista = Revista.objects.get(slug=slug)

    return render(
        request, template_name='revista.html',
        context={'revista': revista}
    )

