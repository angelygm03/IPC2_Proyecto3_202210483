from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def config(request):
    return render(request, "config.html")

def transac(request):
    return render(request, "transac.html")

def peticiones(request):
    return render(request, "peticiones.html")
