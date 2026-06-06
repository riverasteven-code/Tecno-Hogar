from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/', views.product, name='product'),
    path('producto/<slug:slug>/', views.product_detail, name='producto_detalle'),
    path('carrito/', views.car, name='car'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('categorias/', views.categorias, name='categorias'),
    path('agregar-carrito/<int:producto_id>/', views.agregar_carrito, name ='agregar_carrito'),
    path('eliminar_item/<int:item_id>/', views.eliminar_item_carrito, name = 'eliminar_item_carrito' ),
    path('aumentar-cantidad/<int:item_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),
    path('disminuir_cantidad/<int:item_id>/', views.disminuir_cantidad, name='disminuir_cantidad'),
    path('logout/', views.logout_user, name='logout'),
    path('categoria/<slug:slug>/', views.categoria_detalle, name = 'categoria_detalle'),
]