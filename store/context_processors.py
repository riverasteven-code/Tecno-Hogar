from .models import Carrito

def carrito_context(request):
    carrito, creado = Carrito.objects.get_or_create(id=1)

    return {
        'carrito': carrito
    }