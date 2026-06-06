from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Carrito, ItemCarrito
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q

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

    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1') 

        usuario =  authenticate(request, username=email, password=password1)

        if usuario is not None:
            auth_login(request, usuario)
            return redirect('home')


    return render(request, 'store/login.html')

def register(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = email).exists():
            messages.error(request, 'Este correo ya está registrado')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')
        
        usuario = User.objects.create_user(
            username=email,
            email=email,
            password=password1,
            first_name=nombre
        )

        usuario.save()
        return redirect('login')
    
    

    return render(request, 'store/register.html')

def categorias(request):

    query = request.GET.get('q')
    orden = request.GET.get('orden')
    productos = Producto.objects.filter(disponible=True)

    if query:
        productos = productos.filter(
                Q(nombre__icontains = query) |
                Q(marca__icontains = query) |
                Q(descripcion_corta__icontains = query) |
                Q(categoria__nombre__icontains = query)
        )
    
    if orden == 'recientes':
        productos = productos.order_by('-fecha_creacion')
    elif orden == 'antiguos':
        productos = productos.order_by('fecha_creacion')
    elif orden == 'populares':
        productos = productos.order_by('-rating')

    contexto = {
        'productos': productos,
        'query': query,
        'cantidad_productos': productos.count(),
        'orden': orden,
    }
    return render(request, 'store/categorias.html', contexto)

def categoria_detalle (request, slug):
    categoria = get_object_or_404 (Categoria, slug = slug)
    productos = Producto.objects.filter(categoria=categoria, disponible=True)
    orden = request.GET.get('orden')

    if orden == 'recientes':
        productos = productos.order_by('-fecha_creacion')
    elif orden == 'antiguos':
        productos = productos.order_by('fecha_creacion')
    elif orden == 'populares':
        productos = productos.order_by('-rating')

    contexto = {
        'categoria': categoria,
        'productos': productos,
        'cantidad_productos': productos.count(),
        'orden': orden,
    } 

    return render (request, 'store/categorias.html', contexto)

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


def logout_user(request):
    logout(request)
    return redirect('home')


