from django.db import models
from abc import ABC, abstractmethod
from typing import List, Dict, Any


# Modelo para el menú
class Menu(models.Model):
    nombre = models.CharField(max_length=50)  # Nombre del menú
    estado = models.BooleanField()  # Estado del menú (activo/inactivo)

    def __str__(self):
        return self.nombre

    def activar_menu(self) -> None:
        """Activa el menú y guarda el estado."""
        self.estado = True
        self.save()

    def desactivar_menu(self) -> None:
        """Desactiva el menú y guarda el estado."""
        self.estado = False
        self.save()


# Modelo para la categoría dentro de un menú
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)  # Nombre de la categoría
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categorias')  # Relación con el menú

    def __str__(self):
        return self.nombre


# Modelo para un producto dentro de una categoría
class Producto(models.Model):
    nombre = models.CharField(max_length=50)  # Nombre del producto
    descripcion = models.CharField(max_length=255)  # Descripción del producto
    precio = models.FloatField(default=0)  # Precio del producto
    disponibilidad = models.BooleanField()  # Estado de disponibilidad
    cantidad_vendida = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='productos')  # Relación con categoría

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        self.save()

    def __str__(self):
        return self.nombre

    def cambiar_disponibilidad(self, disponible: bool) -> None:
        """Cambia la disponibilidad del producto y guarda el estado."""
        self.disponibilidad = disponible
        self.save()



# Interfaz que define las operaciones del menú
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


# Implementación de la interfaz IMenu
class MenuService(IMenu):

    def agregar_producto(self, categoria_id: int, producto_data: Dict[str, Any]) -> Producto:
        """Agrega un nuevo producto a una categoría específica si no existe ya un producto con el mismo nombre."""
        # Verifica si el producto ya existe en la categoría
        categoria = Categoria.objects.get(id=categoria_id)
        if Producto.objects.filter(nombre=producto_data["nombre"], categoria=categoria).exists():
            raise ValueError(f"El producto '{producto_data['nombre']}' ya existe en esta categoría.")

        # Si el producto no existe, lo crea
        producto = Producto.objects.create(
            nombre=producto_data["nombre"],
            descripcion=producto_data["descripcion"],
            precio=producto_data["precio"],
            disponibilidad=producto_data["disponibilidad"],
            categoria=categoria
        )
        return producto

    def eliminar_producto(self, producto_id: int) -> None:
        """Elimina un producto dado su ID, con verificación de existencia."""
        producto = Producto.objects.filter(id=producto_id).first()
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")

        producto.delete()

    def agregar_categoria(self, menu_id: int, nombre_categoria: str) -> Categoria:
        """Agrega una nueva categoría a un menú existente."""
        menu = Menu.objects.get(id=menu_id)
        categoria = Categoria.objects.create(nombre=nombre_categoria, menu=menu)
        return categoria

    def eliminar_categoria(self, categoria_id: int) -> None:
        """Elimina una categoría dado su ID, con verificación de existencia."""
        categoria = Categoria.objects.filter(id=categoria_id).first()
        if not categoria:
            raise ValueError(f"Categoría con ID {categoria_id} no encontrada.")

        categoria.delete()

    def modificar_categoria(self, categoria_id: int, nuevo_nombre: str) -> None:
        """Modifica el nombre de una categoría."""
        categoria = Categoria.objects.filter(id=categoria_id).first()
        if not categoria:
            raise ValueError(f"Categoría con ID {categoria_id} no encontrada.")

        categoria.nombre = nuevo_nombre
        categoria.save()

    def modificar_producto(self, producto_id: int, producto_data: Dict[str, Any]) -> None:
        """Modifica los atributos de un producto existente, verificando que el producto exista."""
        producto = Producto.objects.filter(id=producto_id).first()
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")

        # Actualiza los campos del producto
        producto.nombre = producto_data["nombre"]
        producto.descripcion = producto_data["descripcion"]
        producto.precio = producto_data["precio"]
        producto.disponibilidad = producto_data["disponibilidad"]
        producto.save()

    def buscar_categoria(self, nombre: str) -> List[Categoria]:
        """Busca categorías cuyo nombre contenga la palabra clave."""
        return list(Categoria.objects.filter(nombre__icontains=nombre))

    def buscar_producto(self, nombre: str) -> List[Producto]:
        """Busca productos cuyo nombre contenga la palabra clave."""
        return list(Producto.objects.filter(nombre__icontains=nombre))

    def mostrar_menu(self, menu_id: int) -> Dict[str, Any]:
        """Retorna un diccionario con la información del menú y sus categorías."""
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
        """Activa el producto (disponibilidad True) y guarda el estado."""
        producto = Producto.objects.get(id=producto_id)
        producto.disponibilidad = True
        producto.save()

    def desactivar_producto(self, producto_id: int) -> None:
        """Desactiva el producto (disponibilidad False) y guarda el estado."""
        producto = Producto.objects.get(id=producto_id)
        producto.disponibilidad = False
        producto.save()

    def mostrar_productos_por_categoria(self, categoria_id: int) -> List[Dict[str, Any]]:
        """Devuelve una lista de todos los productos de una categoría específica."""
        categoria = Categoria.objects.get(id=categoria_id)
        productos = Producto.objects.filter(categoria=categoria)
        return list(productos.values("id", "nombre", "descripcion", "precio", "disponibilidad"))

    def buscar_producto_por_precio(self, min_precio: float, max_precio: float) -> List[Producto]:
        """Busca productos cuyo precio esté dentro del rango especificado."""
        return list(Producto.objects.filter(precio__gte=min_precio, precio__lte=max_precio))
