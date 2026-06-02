from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, ItemCarrito

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

    carrito, creado = Carrito.objects.get_or_create(id=1)
    items = carrito.items.all()

    contexto = {
        'carrito': carrito,
        'items': items
    }

    return render(request, 'store/car.html', contexto)

def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, disponible=True)

    carrito, creado = Carrito.objects.get_or_create(id=1)

    item, creado = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        producto=producto
    )

    if not creado:
        item.cantidad += 1
        item.save()

    return redirect('car')

def login(request):
    return render(request, 'store/login.html')

def register(request):
    return render(request, 'store/register.html')

def categorias(request):
    productos = Producto.objects.filter(disponible=True)
    contexto = {'productos': productos}
    return render(request, 'store/categorias.html', contexto)

def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('car')

def aumentar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.cantidad += 1
    item.save()
    return redirect('car')


def disminuir_cantidad(request, item_id):
    item = get_object_or_404 (ItemCarrito, id=item_id)
    
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()

    return redirect( 'car' )



