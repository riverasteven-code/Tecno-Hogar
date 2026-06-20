# TecnoHogar

## 1. Nombre de la tienda virtual

**TecnoHogar**

TecnoHogar es una tienda virtual enfocada en la venta de productos tecnológicos como laptops, monitores, periféricos, audio, tablets y componentes.

---

## 2. Integrantes del grupo

* Brayan Steven Rivera Poveda

---

## 3. Descripción de la tienda

TecnoHogar es una aplicación web tipo ecommerce desarrollada con Django. La tienda permite a los usuarios visualizar productos tecnológicos, 
consultar categorías, ver el detalle de cada producto, agregar productos al carrito, registrarse, iniciar sesión y finalizar una compra básica.

El proyecto cuenta con un panel administrativo donde se pueden gestionar categorías, productos, carritos, órdenes e items de compra.

---

## 4. Objetivo del proyecto

El objetivo del proyecto es desarrollar una tienda virtual funcional utilizando Django como framework principal, 
MySQL como base de datos y tecnologías web como HTML, CSS, JavaScript y Bootstrap.

El proyecto busca aplicar conceptos de desarrollo web como:

* Creación de modelos.
* Conexión con base de datos.
* Uso de vistas.
* Manejo de rutas.
* Uso de templates.
* Gestión de usuarios.
* Carrito de compras.
* Registro de órdenes.
* Panel administrativo.

---

## 5. Tecnologías utilizadas

* Python 3.10
* Django
* MySQL Server
* MySQL Workbench
* mysqlclient
* HTML5
* CSS3
* JavaScript
* Bootstrap
* Bootstrap Icons-
* Font Awesome
* Visual Studio Code

---

## 6. Estructura del proyecto

La estructura principal del proyecto es la siguiente:

```txt
tecno_hogar/
│
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   │   └── store/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── categorias.html
│   │       ├── product.html
│   │       ├── car.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── compra_exitosa.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── media/
│
├── manage.py
└── README.md
```

### Descripción de carpetas principales

**core/**
Contiene la configuración general del proyecto Django.

**store/**
Contiene la aplicación principal de la tienda, donde están los modelos, vistas, rutas, templates y configuración del admin.

**static/**
Contiene archivos estáticos como CSS, JavaScript e imágenes fijas del diseño.

**media/**
Contiene imágenes subidas desde el panel administrador, como las imágenes de los productos.

---

## 7. Instrucciones de instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto:

```bash
cd tecno_hogar
```

---

### 2. Crear entorno virtual

```bash
py -m venv venv
```

---

### 3. Activar entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

Debe aparecer `(venv)` al inicio de la terminal.

---

### 4. Instalar dependencias

```bash
pip install django mysqlclient pillow
```

También se puede usar:

```bash
pip install -r requirements.txt
```

si el proyecto cuenta con archivo `requirements.txt`.

---

### 5. Crear la base de datos en MySQL

Abrir MySQL Workbench y ejecutar:

```sql
CREATE DATABASE tecno_hogar_db;
```

---

### 6. Configurar la base de datos

En el archivo:

```txt
core/settings.py
```

verificar la configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tecno_hogar_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

> Nota: si el usuario o contraseña de MySQL son diferentes, se deben cambiar en esta sección.

---

### 7. Crear migraciones

```bash
py manage.py makemigrations
```

---

### 8. Aplicar migraciones

```bash
py manage.py migrate
```

Este comando crea las tablas necesarias en la base de datos.

---

### 9. Crear superusuario

```bash
py manage.py createsuperuser
```

Este usuario permite ingresar al panel administrador.

---

### 10. Ejecutar el servidor

```bash
py manage.py runserver
```

Abrir en el navegador:

```txt
http://127.0.0.1:8000/
```

Panel administrador:

```txt
http://127.0.0.1:8000/admin/
```

---

## 8. Funcionalidades implementadas

El proyecto cuenta con las siguientes funcionalidades:

### Página de inicio

* Muestra carrusel principal.
* Muestra categorías.
* Muestra productos en oferta.
* Muestra productos destacados.

### Categorías

* Permite ver todos los productos.
* Permite ver productos por categoría.
* Permite ordenar productos por recientes, antiguos y populares.
* Permite buscar productos por nombre, marca, descripción o categoría.

### Detalle de producto

* Muestra imagen principal del producto.
* Muestra marca, nombre, descripción, precio y stock.
* Muestra características del producto.
* Muestra información adicional.
* Muestra productos relacionados.
* Permite agregar el producto al carrito.

### Carrito de compras

* Permite agregar productos.
* Permite aumentar cantidad.
* Permite disminuir cantidad.
* Permite eliminar productos.
* Calcula subtotal.
* Calcula descuento.
* Calcula total de compra.
* Permite finalizar compra.

### Usuarios

* Permite crear cuenta.
* Permite iniciar sesión.
* Permite cerrar sesión.
* Muestra el nombre del usuario en el navbar cuando ha iniciado sesión.

### Finalizar compra

* Crea una orden.
* Copia los productos del carrito a la orden.
* Guarda el total de la compra.
* Vacía el carrito.
* Muestra una página de compra exitosa.

### Panel administrador

Desde el panel administrador se pueden gestionar:

* Categorías.
* Productos.
* Carrito.
* Items del carrito.
* Órdenes.
* Items de órdenes.
* Usuarios.

---

## 9. Flujo de información

El flujo principal del proyecto funciona de la siguiente manera:

```txt
Usuario entra a la página
        ↓
Django recibe la URL
        ↓
store/urls.py conecta la ruta con una vista
        ↓
views.py ejecuta la lógica
        ↓
models.py consulta o guarda información en MySQL
        ↓
La vista envía datos al template
        ↓
El HTML muestra la información al usuario
```

### Ejemplo: flujo de productos en home

```txt
Usuario entra a /
        ↓
Se ejecuta la vista home
        ↓
La vista consulta productos disponibles
        ↓
Los productos se envían a home.html
        ↓
home.html muestra ofertas y destacados
```

### Ejemplo: flujo del carrito

```txt
Usuario presiona "Agregar al carrito"
        ↓
Se ejecuta agregar_carrito
        ↓
Django busca el producto
        ↓
Django crea o actualiza ItemCarrito
        ↓
El usuario entra a /carrito/
        ↓
car.html muestra productos, cantidades y total
```

### Ejemplo: flujo de compra

```txt
Usuario presiona "Finalizar compra"
        ↓
Se ejecuta finalizar_compra
        ↓
Se crea una Orden
        ↓
Se crean ItemOrden
        ↓
Se vacía el carrito
        ↓
Se muestra compra_exitosa.html
```

---

## 10. Pruebas realizadas

Se realizaron pruebas manuales para verificar el funcionamiento del proyecto.

### Pruebas de navegación

* Se verificó que la página de inicio cargara correctamente.
* Se verificó que el navbar funcionara.
* Se verificó que los enlaces a categorías funcionaran.
* Se verificó que el footer se mostrara correctamente.

### Pruebas de productos

* Se verificó que los productos se mostraran desde la base de datos.
* Se verificó que los productos destacados aparecieran en el home.
* Se verificó que los productos en oferta aparecieran correctamente.
* Se verificó que el detalle de producto cargara según el slug.

### Pruebas de categorías

* Se verificó que cada categoría mostrara sus productos correspondientes.
* Se verificó el contador de productos encontrados.
* Se verificó el ordenamiento por productos recientes, antiguos y populares.

### Pruebas de búsqueda

* Se realizaron búsquedas por nombre.
* Se realizaron búsquedas por marca.
* Se realizaron búsquedas por categoría.
* Se comprobó que los resultados coincidieran con la búsqueda.

### Pruebas del carrito

* Se agregó un producto al carrito.
* Se agregó varias veces el mismo producto.
* Se aumentó la cantidad de productos.
* Se disminuyó la cantidad.
* Se eliminó un producto.
* Se verificó el subtotal.
* Se verificó el total.
* Se verificó el descuento.

### Pruebas de usuario

* Se creó una cuenta nueva.
* Se verificó que no se pudiera registrar un correo repetido.
* Se verificó que las contraseñas debían coincidir.
* Se inició sesión correctamente.
* Se cerró sesión correctamente.

### Pruebas de compra

* Se agregó un producto al carrito.
* Se finalizó la compra.
* Se verificó que se creara una orden.
* Se verificó que se crearan items de orden.
* Se verificó que el carrito quedara vacío.
* Se verificó que apareciera la página de compra exitosa.

---

## 11. Enlace del video de sustentación

Enlace del video:

```txt
PEGAR AQUÍ EL ENLACE DEL VIDEO DE SUSTENTACIÓN
```

## Conclusión

TecnoHogar es una tienda virtual desarrollada con Django y MySQL que permite manejar productos, categorías, usuarios, carrito de compras y órdenes.

El proyecto conecta backend, base de datos y frontend mediante modelos, vistas, rutas y templates. Además, permite administrar la información desde el panel de Django 
y simula el flujo básico de compra de una tienda virtual.