from django.contrib import admin
from .models import Categoria, Producto, Carrito, CarritoProducto, Pedido
from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'stock']

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['id', 'total']

@admin.register(CarritoProducto)
class CarritoProductoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'carrito', 'cantidad']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'estado']
