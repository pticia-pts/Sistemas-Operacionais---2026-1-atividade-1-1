from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (request):
    return HttpResponse("Olá, Professor! Sou sua aluna Patricia Pontes em SO!")

