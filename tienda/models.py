
from django.db import models
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)



class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Carrito {self.id}"

class CarritoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"

class Pedido(models.Model):
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
    )
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='Pendiente')

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"
