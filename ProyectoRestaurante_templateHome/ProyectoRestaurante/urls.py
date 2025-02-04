from django.contrib import admin
from django.urls import path, include
from mesas import views as mesas_views  # Alias para las vistas de mesas
from menu import views as menu_views  # Alias para las vistas de menú
from estadisticas import views as estadisticas_views
from menu.views import categories_view, meals_view, convertir_divisa
from pedidos import views as pedidos_views  # Alias para las vistas de pedidos

urlpatterns = [
    path('AdminIndividual/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', mesas_views.home, name='home'),  # Usando alias para vistas de mesas

    path('login/', mesas_views.login_view, name='login'),
    path('register/', mesas_views.register, name='register'),
    path('logout/', mesas_views.logout_view, name='logout'),

    path('menu/', menu_views.gestionar_menu, name='gestionar_menu'),  # Usando alias para vistas de menú
    path('estadistica/', estadisticas_views.estadistica, name='estadistica'),
    path('estadisticas/meseros/', estadisticas_views.estadisticas_meseros, name='estadisticas_meseros'),
    path('estadisticas/mesas/', estadisticas_views.estadisticas_mesas, name='estadisticas_mesas'),
    path('estadisticas/productos/', estadisticas_views.estadisticas_productos, name='estadisticas_productos'),
    path('estadisticas/ventastotales/', estadisticas_views.ventas_totales, name='ventas_totales'),
    path('estadisticas/reportes/', estadisticas_views.reportes, name='reportes'),
    path('estadisticas/reporte_pdf/', estadisticas_views.reporte_pdf, name='reporte_pdf'),

    path('homeAdmin/', mesas_views.homeAdmin, name='homeAdmin'),
    path('listar_mesas/', mesas_views.listar_mesas.as_view(), name='listar_mesas'),
    path('editar_mesas/<int:pk>/', mesas_views.edicion_mesas.as_view(), name='editar_mesas'),
    path('crear_mesa/', mesas_views.crear_mesa.as_view(), name='crear_mesa'),
    path('eliminar_mesa/<int:pk>/', mesas_views.eliminar_mesa, name='eliminar_mesa'),

    path('listar_menu/', menu_views.listar_menu.as_view(), name='listar_menu'),
    path('editar_menu/<int:pk>/', menu_views.edicion_menu.as_view(), name='editar_menu'),
    path('crear_menu/', menu_views.crear_menu, name='crear_menu'),
    path('menu/<int:pk>/eliminar/', menu_views.eliminar_menu, name='eliminar_menu'),
    path('menu/<int:pk>/categorias/', menu_views.listar_categorias.as_view(), name='listar_categorias'),
    path('categorias/<int:pk>/editar/', menu_views.edicion_categoria.as_view(), name='editar_categoria'),
    path('categorias/crear/', menu_views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:pk>/eliminar/', menu_views.eliminar_categoria, name='eliminar_categoria'),
    path('categorias/<int:pk>/productos/', menu_views.listar_productos.as_view(), name='listar_productos'),
    path('productos/<int:pk>/editar/', menu_views.edicion_producto.as_view(), name='editar_producto'),
    path('productos/crear/', menu_views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/eliminar/', menu_views.eliminar_producto, name='eliminar_producto'),
    path('menus/', include('menu.urls')),
    path('convertir/', convertir_divisa, name='convertir_divisa'),
    path('reservas/', mesas_views.listar_reservas, name='listar_reservas'),
    path('reservas/crear/', mesas_views.crear_reserva, name='crear_reserva'),
    path('reservas/cancelar/<int:reserva_id>/', mesas_views.cancelar_reserva, name='cancelar_reserva'),
    path('pedidos/', pedidos_views.gestionar_pedidos, name='gestionar_pedidos'),  # Añadido para pedidos
]
