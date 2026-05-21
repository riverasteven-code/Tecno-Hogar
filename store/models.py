from django.db import models
from django.urls import reverse

# Aquí crearemos la clase Categoria

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    # Habilidad 1: Presentarse con su nombre

    def __str__(self):
        return self.nombre
    
    # Habilidad 2: Dar su dirección web
    def get_absolute_url(self):
        return reverse('categoria_detalle', args=[self.slug])

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.TextField()
    especificaciones = models.TextField(blank=True, help_text="Procesador, RAM, almacenmiento,etc. ")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('producto_detalle', args=[self.slug])