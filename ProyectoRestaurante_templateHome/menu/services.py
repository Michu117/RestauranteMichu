# menus/services.py
from .models import Menu, Categoria, Producto
from typing import Dict, Any, List
import requests
from django.conf import settings


class MenuService:
    def __init__(self):
        # Inicialización de la clase, no necesita nada en este caso
        pass

    def agregar_producto(self, categoria_id: int, producto_data: Dict[str, Any]) -> Producto:
        """
        Agrega un nuevo producto a una categoría específica.

        :param categoria_id: ID de la categoría donde agregar el producto.
        :param producto_data: Diccionario con los datos del producto (nombre, descripción, precio, etc.).
        :return: El objeto Producto creado.
        """
        # Buscar la categoría
        categoria = Categoria.objects.get(id=categoria_id)

        # Crear un nuevo producto
        producto = Producto.objects.create(
            nombre=producto_data["nombre"],
            descripcion=producto_data["descripcion"],
            precio=producto_data["precio"],
            disponibilidad=producto_data["disponibilidad"],
            categoria=categoria
        )
        return producto

    def eliminar_producto(self, producto_id: int) -> None:
        """
        Elimina un producto por su ID.

        :param producto_id: ID del producto a eliminar.
        """
        Producto.objects.filter(id=producto_id).delete()

    def agregar_categoria(self, menu_id: int, nombre_categoria: str) -> Categoria:
        """
        Agrega una nueva categoría a un menú.

        :param menu_id: ID del menú al cual se le agregará la categoría.
        :param nombre_categoria: Nombre de la categoría a agregar.
        :return: La categoría creada.
        """
        menu = Menu.objects.get(id=menu_id)
        categoria = Categoria.objects.create(nombre=nombre_categoria, menu=menu)
        return categoria

    def eliminar_categoria(self, categoria_id: int) -> None:
        """
        Elimina una categoría por su ID.

        :param categoria_id: ID de la categoría a eliminar.
        """
        Categoria.objects.filter(id=categoria_id).delete()

    def modificar_categoria(self, categoria_id: int, nuevo_nombre: str) -> None:
        """
        Modifica el nombre de una categoría.

        :param categoria_id: ID de la categoría a modificar.
        :param nuevo_nombre: El nuevo nombre para la categoría.
        """
        Categoria.objects.filter(id=categoria_id).update(nombre=nuevo_nombre)

    def modificar_producto(self, producto_id: int, producto_data: Dict[str, Any]) -> None:
        """
        Modifica los atributos de un producto existente.

        :param producto_id: ID del producto a modificar.
        :param producto_data: Diccionario con los nuevos datos del producto.
        """
        Producto.objects.filter(id=producto_id).update(
            nombre=producto_data["nombre"],
            descripcion=producto_data["descripcion"],
            precio=producto_data["precio"],
            disponibilidad=producto_data["disponibilidad"]
        )

    def buscar_categoria(self, nombre: str) -> List[Categoria]:
        """
        Busca categorías cuyo nombre contenga la palabra clave.

        :param nombre: Nombre de la categoría para buscar.
        :return: Lista de categorías encontradas.
        """
        return list(Categoria.objects.filter(nombre__icontains=nombre))

    def buscar_producto(self, nombre: str) -> List[Producto]:
        """
        Busca productos cuyo nombre contenga la palabra clave.

        :param nombre: Nombre del producto para buscar.
        :return: Lista de productos encontrados.
        """
        return list(Producto.objects.filter(nombre__icontains=nombre))

    def mostrar_menu(self, menu_id: int) -> Dict[str, Any]:
        """
        Retorna un diccionario con la información del menú y sus categorías.

        :param menu_id: ID del menú a mostrar.
        :return: Diccionario con la información del menú y sus categorías.
        """
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
#api
def obtener_tasas_de_cambio(base_currency):
    url = f'https://v6.exchangerate-api.com/v6/{settings.EXCHANGERATE_API_KEY}/latest/{base_currency}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None