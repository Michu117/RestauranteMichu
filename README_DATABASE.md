# Base de Datos
Elección e Implementación de la Base de Datos utilizada en el proyecto.

## Integración con la base de datos
La base de datos seleccionada para nuestro proyecto fue MySQL.
### ¿Qué es MySQL?
MySQL es un sistema de gestión de bases de datos relacionales de código abierto. Al igual que con otras bases de datos relacionales, MySQL almacena los datos en tablas formadas por filas y columnas. Los usuarios pueden definir, manipular, controlar y consultar datos con el lenguaje de consulta estructurada, también conocido como SQL. Gracias a que MySQL es de código abierto, incluye numerosas funciones desarrolladas en estrecha colaboración con los usuarios durante más de 25 años.

### ¿Por qué elegimos MySQL?
MySQL representa una buena alternativa de base de datos para una aplicación en Django gracias a su desempeño, escalabilidad y compatibilidad. Es una extensamente empleada base de datos relacional de código abierto, que facilita transacciones, replicación y una alta disponibilidad. Adicionalmente, su vinculación con Django es fácil a través de las librerías mysqlclient o PyMySQL. En resumen, nos proporciona alta rapidez en las consultas, es fiable para aplicaciones de gran tráfico y cuenta con una comunidad dinámica que ofrece un extenso soporte y documentación.

## Implementación de la Base de Datos en el Proyecto:
La base de datos fue ejecutada de forma local a través del programa Laragon, para lo cual se configuró de la siguiente manera:
![image](https://github.com/user-attachments/assets/b04506e8-e1d5-4810-ae89-a8f6494342d7)

Como se observa en la figura, la sesión se nombró AppRestaurante y se configuró utilizando MariaDB or MySQL utilizando libmariadb.dll, los demás parámetros están por defecto como se ve en la imagen.

![image](https://github.com/user-attachments/assets/eed8c7be-8553-44c6-8f4c-7e57d38a0073)

En la siguiente figura observamos como se integra la base de datos MySQL con nuestro proyecto Django, para lo cual se necesita realizar esa configuración en el archivo settings.py del proyecto basándonos en las configuraciones establecidas en Laragon y utilizando la librería mysqlclient para la comunicación con Django.

![database image](https://github.com/user-attachments/assets/a02f227a-b5a4-4b47-b5f5-6e7f3e98f66e)

En la última imagen se observa la base de datos en funcionamiento, se puede evidenciar como se registra un Cliente como Persona. Además en la tabla de la izquierda se puede observar todas las tablas creadas por las migraciones.