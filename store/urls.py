from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/', views.product, name='product'),
    path('carrito/', views.car, name='car'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('categorias/', views.categorias, name='categorias'),
]