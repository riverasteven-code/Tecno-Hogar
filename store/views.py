from django.shortcuts import render
from .models import Producto

def home(request):
    productos = Producto.objects.filter(disponible=True)
    contexto = {'productos': productos}
    return render(request, 'store/home.html', contexto)

def product(request):
    return render(request, 'store/product.html')