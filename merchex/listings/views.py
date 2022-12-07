from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous aimons merch!</p>')

def listings(request):
    return HttpResponse('<h2> Liste des annonces pour les articles</h2>')

def contactus(request):
    return HttpResponse('<p>Contactez nous ici</p>')