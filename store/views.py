from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    productos = Producto.objects.filter(disponible=True)
    contexto = {'productos': productos}
    return render(request, 'store/home.html', contexto)

def product_detail(request, slug):
    producto = get_object_or_404(Producto, slug = slug, disponible = True)

    productos_relacionados = Producto.objects.filter (
        categoria = producto.categoria,
        disponible = True
    ).exclude (id = producto.id)[:6]

    contexto = {
        'producto': producto,
        'productos_relacionados' : productos_relacionados
    }

    return render(request, 'store/product.html', contexto)

def product(request):
    return render(request, 'store/product.html')

def car(request):
    return render(request, 'store/car.html')

def login(request):
    return render(request, 'store/login.html')

def register(request):
    return render(request, 'store/register.html')

def categorias(request):
    productos = Producto.objects.filter(disponible=True)
    contexto = {'productos': productos}
    return render(request, 'store/categorias.html', contexto)



