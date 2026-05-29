from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.filter(disponible=True)
    contexto = {'productos': productos}
    return render(request, 'store/home.html', contexto)

def product(request):
    return render(request, 'store/product.html')

def car(request):
    return render(request, 'store/car.html')

def login(request):
    return render(request, 'store/login.html')

def register(request):
    return render(request, 'store/register.html')

def categorias(request):
    return render(request, 'store/categorias.html')