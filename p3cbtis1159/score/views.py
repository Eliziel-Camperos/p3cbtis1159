from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")
def contactos(request):
    return render(request,"contactos.html")
def empleados(request):
    return render(request,"empleados.html")
def Ventas(request):
    return render(request,"Ventas.html")
def Mercancia(request):
    return render(request,"Mercancia.html")
def Comics(request):
    return render(request,"Comics.html")
def Eliziel(request):
    return HttpResponse("Hola Soy Eliziel")
def minovia(request):
    return HttpResponse("aqui va mi novia, si tan solo tuviera una")