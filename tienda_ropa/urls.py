from django.contrib import admin
from django.urls import path, include
from tienda import views  # Importa las vistas de tu aplicación
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
