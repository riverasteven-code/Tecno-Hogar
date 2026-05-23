from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/', views.product, name='product'),
    path('carrito/', views.car, name='car'),
]