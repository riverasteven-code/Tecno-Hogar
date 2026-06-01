from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'slug')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = (
        'nombre', 
        'marca',
        'categoria',
        'precio',
        'precio_anterior', 
        'stock', 
        'disponible',
        'destacado',
        'oferta',
    )
    list_filter = (
        'categoria', 
        'marca',
        'disponible',
        'destacado',
        'oferta',
    )
    search_fields = (
        'nombre',
        'marca',
        'descripcion_corta',
    )