# RestauranteMichu - Menuboard - EvaluaciónU3
Aplicación de Gestión de Restaurante.
# Autores - Grupo 6
- Arelys Anahi Ajila Apolo.
- Douglas Andrey Carreño Pardo.
- Viviana Elizabeth Córdova Celi.
- Fabricio Josue Ruiz Aguilar.
- Maria del Cisne Valarezo Román.
# Componentes Clave
1. Implementación de la Interfaz Gráfica de Usuario (GUI).
2. Integración con una Base de Datos y Operaciones CRUD.
3. Uso de APIs o Librerías Estándar.
4. Pruebas de Integración y Funcionalidad.
5. Reflexión Escrita Final.
## Modulos
-[Modulo de Reportes y Estadistica](ProyectoRestaurante_templateHome/estadisticas/models.py)

Este modulo, brinda la informacion del desempeño del restaurante, a travez de reportes y estadisticas que seran proporcionados en graficos dinamicos y archivos PDF. Incluyen productos mas vendido, mesa mas usada , desempeño de empleados y ventas totales. Esta informacion se genera a partir del ingreso en un rango de fechas establecidos por el administrador.


-[Modulo de Facturacion y Pagos](ProyectoRestaurante_templateHome/facturacion/models.py)

Este modulo, permite la generacion de una factura, la cual por defecto calcula el total del pedido, incluyendo impuestos y descuentos, ademas de generar el tipo de pago por el cual se tramita la factura, tambien permite registrar todas las facturas emitidas. Este modulo, solo puede ser accedido por el administrador


-[Modulo de Inventario](ProyectoRestaurante_templateHome/inventario/models.py)

Este modulo, inventario, permite la gestion de  los insumos y productos necesarios para la preparación de los platos del restaurante. Cada insumo esta registrado con nombre, cantidad disponible y unidad de medida. el sistemas permite el ingreso de entradas de nuevos insumos y salidas de los mismos. Además, genera alertas cuando el insumo de inventario esté bajo o agotado. solo accesible para administrador


-[Modulos de Menús y Productos](ProyectoRestaurante_templateHome/menu/models.py)

Este módulo gestiona los productos y platos que se ofrecen en el restaurante. Cada producto tiene atributos como nombre, descripción, categoría, precio y disponibilidad. El menú esta organizado por categorías, El sistema permitir agregar nuevos productos al menú, modificarlos o eliminarlos.


-[Modulos de Pedidos](ProyectoRestaurante_templateHome/pedidos/models.py)

El módulo de pedidos permite gestionar los pedidos de los clientes, desde que se realiza el pedido hasta que es servido y pagado. Cada pedido puede contener uno o más productos del menú, y es posible agregar o eliminar productos mientras el pedido no haya sido servido. El sistema permiti modificar cantidades de productos en los pedidos, así como su estado. este modulo interactura con el usuario



-[Modulo de Mesas y reservaciones](ProyectoRestaurante_templateHome/mesas/models.py)

Este módulo gestiona la disponibilidad y uso de las mesas dentro del restaurante. Las mesas pueden estar en diferentes estados, tales como libre, ocupada o reservada. Los clientes pueden hacer reservaciones especificando la fecha y hora de la reserva. par lograr identificar  cada mesa, como el número de asientos y su ubicación en el restaurante. Cuando un cliente llega, una mesa puede ser asignada, y al finalizar su uso, la mesa debe ser liberada para otros clientes. Las reservaciones pueden ser modificadas o canceladas por el cliente o el personal del restaurante.este modulo interactura directamente con el usuario

## Diagramas de Clases 
### Diagrama de Clases estadística
![Image](https://github.com/user-attachments/assets/16dd532f-568f-4bb7-8717-8682cb696e83)
## Diagrama de Clases facturación
![Image](https://github.com/user-attachments/assets/5348c18a-c896-4a32-9606-f6f181da32c0)
## Diagrama de Clases Inventario
![Image](https://github.com/user-attachments/assets/b4e186e8-861e-4138-b4e7-0797f8fbf1f1)
## Diagrama de Clases Menú
![Image](https://github.com/user-attachments/assets/60c3cd7a-04e2-412d-bb4f-0ab1d1318808)
## Diagrama de Clases Pedido
![Image](https://github.com/user-attachments/assets/d1191f78-eada-4271-80b4-b04e8aa98dea)
## Diagrama de Clases Mesa
![Image](https://github.com/user-attachments/assets/1b5c4b63-2b6b-4ef8-9e54-e68d4f93ce48)
