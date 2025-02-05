from django.db import models
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

    def activar_menu(self) -> None:
        self.estado = True
        self.save()

    def desactivar_menu(self) -> None:
        self.estado = False
        self.save()


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categorias')

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField(default=0)
    disponibilidad = models.BooleanField()
    cantidad_vendida = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        self.save()

    def __str__(self):
        return self.nombre

    def cambiar_disponibilidad(self, disponible: bool) -> None:
        self.disponibilidad = disponible
        self.save()


class IMenu(ABC):

    @abstractmethod
    def agregar_producto(self, categoria_id: int, producto_data: Dict[str, Any]) -> Producto:
        pass

    @abstractmethod
    def eliminar_producto(self, producto_id: int) -> None:
        pass

    @abstractmethod
    def agregar_categoria(self, menu_id: int, nombre_categoria: str) -> Categoria:
        pass

    @abstractmethod
    def eliminar_categoria(self, categoria_id: int) -> None:
        pass

    @abstractmethod
    def modificar_categoria(self, categoria_id: int, nuevo_nombre: str) -> None:
        pass

    @abstractmethod
    def modificar_producto(self, producto_id: int, producto_data: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def buscar_categoria(self, nombre: str) -> List[Categoria]:
        pass

    @abstractmethod
    def buscar_producto(self, nombre: str) -> List[Producto]:
        pass

    @abstractmethod
    def mostrar_menu(self, menu_id: int) -> Dict[str, Any]:
        pass


class MenuService(IMenu):

    def agregar_producto(self, categoria_id: int, producto_data: Dict[str, Any]) -> Producto:
        categoria = Categoria.objects.get(id=categoria_id)
        if Producto.objects.filter(nombre=producto_data["nombre"], categoria=categoria).exists():
            raise ValueError(f"El producto '{producto_data['nombre']}' ya existe en esta categoría.")

        producto = Producto.objects.create(
            nombre=producto_data["nombre"],
            descripcion=producto_data["descripcion"],
            precio=producto_data["precio"],
            disponibilidad=producto_data["disponibilidad"],
            categoria=categoria
        )
        return producto

    def eliminar_producto(self, producto_id: int) -> None:
        producto = Producto.objects.filter(id=producto_id).first()
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")

        producto.delete()

    def agregar_categoria(self, menu_id: int, nombre_categoria: str) -> Categoria:
        menu = Menu.objects.get(id=menu_id)
        categoria = Categoria.objects.create(nombre=nombre_categoria, menu=menu)
        return categoria

    def eliminar_categoria(self, categoria_id: int) -> None:
        categoria = Categoria.objects.filter(id=categoria_id).first()
        if not categoria:
            raise ValueError(f"Categoría con ID {categoria_id} no encontrada.")

        categoria.delete()

    def modificar_categoria(self, categoria_id: int, nuevo_nombre: str) -> None:
        categoria = Categoria.objects.filter(id=categoria_id).first()
        if not categoria:
            raise ValueError(f"Categoría con ID {categoria_id} no encontrada.")

        categoria.nombre = nuevo_nombre
        categoria.save()

    def modificar_producto(self, producto_id: int, producto_data: Dict[str, Any]) -> None:
        producto = Producto.objects.filter(id=producto_id).first()
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")

        producto.nombre = producto_data["nombre"]
        producto.descripcion = producto_data["descripcion"]
        producto.precio = producto_data["precio"]
        producto.disponibilidad = producto_data["disponibilidad"]
        producto.save()

    def buscar_categoria(self, nombre: str) -> List[Categoria]:
        return list(Categoria.objects.filter(nombre__icontains=nombre))

    def buscar_producto(self, nombre: str) -> List[Producto]:
        return list(Producto.objects.filter(nombre__icontains=nombre))

    def mostrar_menu(self, menu_id: int) -> Dict[str, Any]:
        menu = Menu.objects.get(id=menu_id)
        categorias = Categoria.objects.filter(menu=menu)
        return {
            "menu": menu.nombre,
            "estado": menu.estado,
            "categorias": [
                {
                    "nombre": cat.nombre,
                    "productos": list(cat.productos.values("nombre", "descripcion", "precio", "disponibilidad"))
                } for cat in categorias
            ]
        }

    def activar_producto(self, producto_id: int) -> None:
        producto = Producto.objects.get(id=producto_id)
        producto.disponibilidad = True
        producto.save()

    def desactivar_producto(self, producto_id: int) -> None:
        producto = Producto.objects.get(id=producto_id)
        producto.disponibilidad = False
        producto.save()

    def mostrar_productos_por_categoria(self, categoria_id: int) -> List[Dict[str, Any]]:
        categoria = Categoria.objects.get(id=categoria_id)
        productos = Producto.objects.filter(categoria=categoria)
        return list(productos.values("id", "nombre", "descripcion", "precio", "disponibilidad"))

    def buscar_producto_por_precio(self, min_precio: float, max_precio: float) -> List[Producto]:
        return list(Producto.objects.filter(precio__gte=min_precio, precio__lte=max_precio))
