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
    marca = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion_corta = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField()
    especificaciones = models.TextField(blank=True, help_text="Procesador, RAM, almacenamiento, etc.")    
    beneficios = models.TextField(blank=True)
    pantalla = models.CharField(max_length=150, blank=True)
    procesador = models.CharField(max_length=100, blank=True)    
    procesador_descripcion = models.CharField(max_length=225, blank=True)
    memoria_ram = models.CharField(max_length=100, blank=True)
    memoria_ram_descripcion = models.CharField(max_length=255, blank=True)
    almacenamiento = models.CharField(max_length=100, blank=True)
    almacenamiento_descripcion = models.CharField(max_length=255, blank=True)
    diseno = models.CharField(max_length=255, blank=True)
    serie = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    garantia = models.CharField(max_length=100, blank=True)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    num_resenas = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    disponible = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    oferta = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('producto_detalle', args=[self.slug])