# API Menuboard
Investigación e integración de un API público para aplicaciones de restaurantes.

# APIs Investigadas

## 1. OpenWeather - Weather API 
### Current Weather Data:
- Acceda a datos meteorológicos actuales de cualquier ubicación.
- Se recopilan y procesan datos meteorológicos de diferentes fuentes, como modelos meteorológicos globales y locales, satélites, radares y una amplia red de estaciones meteorológicas.
- Formatos JSON, XML y HTML.
- Incluido en suscripciones gratuitas y de pago.

[Documentación](https://openweathermap.org/current)

### Funcionalidades:
La API de OpenWeatherMap permite acceder a datos meteorológicos actuales de cualquier parte del mundo. Sus funcionalidades clave incluyen:

- **Consulta de datos meteorológicos actuales:** Proporciona información sobre temperatura, humedad, presión, velocidad del viento, nubosidad, visibilidad y fenómenos meteorológicos (lluvia, nieve, etc.).
- **Formatos de respuesta:** Soporta JSON (por defecto), XML y HTML.
- **Parámetros adicionales:** Permite definir unidades de medida (standard, metric, imperial) y soporte para múltiples idiomas.
- **API de geocodificación:** Convierte nombres de ciudades y códigos postales en coordenadas geográficas y viceversa.
- **Descarga masiva:** Permite obtener grandes volúmenes de datos sin necesidad de realizar llamadas a la API en tiempo real.

### Requisitos:
- Clave API (```appid```) obligatoria para autenticar las solicitudes.

Parámetros requeridos:
- ```lat``` y ```lon``` para coordenadas geográficas.
- ```q``` para nombre de ciudad (con código de país opcional).
- ```id``` para identificador de ciudad.
- ```zip``` para código postal (requiere código de país si no es EE.UU.).

### Limitaciones
- **Obsolescencia de ciertas funciones:** La geocodificación integrada y la búsqueda por nombre de ciudad han quedado obsoletas y no recibirán actualizaciones.
- **Visibilidad limitada:** Máximo de 10 km.
- **Restricción de llamadas:** Dependiendo del plan contratado, puede haber límites en la cantidad de solicitudes permitidas por minuto.
- 1000 llamadas API por día de forma gratuita y 0,0015 USD por llamada API por encima del límite diario.

## 2. TheMealDB
TheMealDB es una API RESTful que proporciona una base de datos abierta y colaborativa de recetas de todo el mundo.

[Documentación](https://www.themealdb.com/api.php)
### Funcionalidades:
- **Búsqueda de recetas por nombre:** Permite buscar recetas específicas utilizando el nombre del plato.
- **Listado de recetas por letra inicial:** Ofrece la posibilidad de listar todas las recetas que comienzan con una letra específica.
- **Obtener detalles completos de una receta por ID:** Proporciona información detallada de una receta específica mediante su identificador único.
- **Obtener una receta aleatoria:** Devuelve una receta seleccionada al azar.
- **Listar todas las categorías, áreas e ingredientes:** Facilita la obtención de listas completas de categorías de platos, áreas culinarias e ingredientes disponibles en la base de datos.
- **Filtrar recetas por ingrediente principal, categoría o área:** Permite filtrar recetas basándose en un ingrediente específico, una categoría de plato o una región culinaria.

### Requisitos:
- Clave API de prueba: Durante el desarrollo o para uso educativo, se puede utilizar la clave de prueba "1".

- Clave API de producción: Para aplicaciones que se lanzarán públicamente, es necesario convertirse en patrocinador para obtener una clave de producción. Los patrocinadores tienen acceso a funciones adicionales, como la capacidad de filtrar por múltiples ingredientes y agregar sus propias recetas e imágenes.

### Limitaciones
- **Acceso limitado para usuarios no patrocinadores:** Algunas funcionalidades avanzadas, como la selección de 10 recetas aleatorias, las últimas recetas añadidas y el filtrado por múltiples ingredientes, están disponibles únicamente para patrocinadores.

- **Sin límite de tasa conocido:** Actualmente, no se ha informado de un límite de solicitudes para la API, lo que facilita su uso en aplicaciones de desarrollo.

## 3. ExchangeRate-API
La ExchangeRate-API es una herramienta que proporciona datos de tipos de cambio de divisas a través de una API sencilla y rápida.

[Documentación](https://www.exchangerate-api.com/docs/overview)
### Funcionalidades:
- **Endpoint Estándar:** Permite obtener un objeto JSON con los tipos de cambio desde una moneda base a todas las demás monedas soportadas. 
- **Conversión de Pares:** Al enviar un par de códigos de moneda y una cantidad opcional, la API devuelve el tipo de cambio entre esas dos monedas y la conversión de la cantidad proporcionada. 
- **Datos Enriquecidos:** Ofrece información adicional como el nombre de la moneda, su símbolo, el país o región asociado y una URL de la bandera correspondiente. Esta funcionalidad está disponible para usuarios en los planes Business o Volume. 
- **Datos Históricos:** Permite acceder a tipos de cambio de fechas específicas en el pasado, con datos disponibles desde 1990 para algunos pares de monedas. Esta característica también está reservada para usuarios en los planes Business o Volume. 

### Requisitos:
- **Clave de API:** Para acceder a la mayoría de las funcionalidades, es necesario registrarse y obtener una clave de API. Sin embargo, existe un endpoint de acceso abierto que no requiere clave, aunque está sujeto a términos específicos y requiere atribución. 

### Limitaciones
- **Frecuencia de Actualización:** La frecuencia de actualización de los datos puede variar según el plan seleccionado. Los planes gratuitos pueden tener actualizaciones menos frecuentes en comparación con los planes de pago. 
- **Acceso a Funcionalidades Avanzadas:** Características como datos enriquecidos y datos históricos están disponibles únicamente para usuarios en los planes Business o Volume. 
- **Límites de Solicitudes:** Dependiendo del plan, existen límites en la cantidad de solicitudes que se pueden realizar a la API. Es importante revisar estos límites para asegurarse de que se ajusten a las necesidades de la aplicación.

# Propuesta de Integración:
## APIs Seleccionadas: TheMealDB y ExchangeRate
Incorporarmos TheMealDB y ExchangeRate-API en la aplicación de restaurante para mejorar la gestión del menú, y poder convertir la moneda para que cada cliente pueda saber el precio que tendría ese producto en su país. De esta forma permitiendo a los clientes explorar platos, ingredientes y recetas con detalles enriquecidos.
## Mejoras al sistema
### TheMealDB API:
TheMealDB es una API que proporciona acceso a una extensa base de datos de recetas, ingredientes e imágenes de platillos internacionales. Permite a los usuarios explorar platos de diferentes categorías y países, obtener detalles completos sobre cada platillo, incluyendo su nombre, ingredientes y métodos de preparación.
### ExchangeRate-API:
ExchangeRate-API ofrece acceso a tasas de cambio de divisas en tiempo real, permitiendo convertir cantidades entre diferentes monedas. Esta API es útil para restaurantes que reciben pagos internacionales o compran insumos de otros países, ya que permite realizar conversiones precisas de precios y costos en función de las tasas de cambio actuales.

# Implementación y Funcionamiento

Las APIs fueron implementadas en la App menu.

## TheMealsDB
1. http://localhost:8000/menus/categorias/

![image](https://github.com/user-attachments/assets/d5b99ad2-512a-4303-bdb7-d70b460433af)

En este apartado se pueden observar todas las categorías.

![image](https://github.com/user-attachments/assets/a2766f73-4c4e-4f93-bdb0-83ae028c6053)

Es la función encargada de obtener las categorías directo desde la API.

![image](https://github.com/user-attachments/assets/1b45a1bc-0e02-4779-a8c2-b39f7eafbaab)

Es la función encargada de mostrar las categorías obtenidas directo desde la API.

2. http://localhost:8000/menus/categorias/Dessert/

![image](https://github.com/user-attachments/assets/321bb8db-cbcb-45d0-8c65-453d4acb051d)

En este apartado se pueden observar todos los platos dentro de la categoría seleccionada.

![image](https://github.com/user-attachments/assets/e52762f5-35f6-4d8e-9cb9-ddc046c8be2b)

Es la función encargada de obtener los platos por categorías directo desde la API.

![image](https://github.com/user-attachments/assets/27b6e805-1722-4d48-a331-899aec312eda)

Es la función encargada de mostrar los platos por categorías obtenidas directo desde la API.

3. http://localhost:8000/menus/menus/52767/

![image](https://github.com/user-attachments/assets/c73a6f63-9582-44a9-82ef-b90bc985fa24)

![image](https://github.com/user-attachments/assets/df802a26-b31e-4b78-8cb2-f9a1a8350123)

![image](https://github.com/user-attachments/assets/6dc99177-e414-444e-841d-de33440b4305)

En este apartado se pueden observar datos específicos de los platos dentro de la categoría seleccionada como lo son:
- Detalles del Plato.
- Ingredientes.
- Instrucciones

![image](https://github.com/user-attachments/assets/2c284fc3-7495-4110-b7a2-43fe9ed4e684)

Es la función encargada de obtener los detalles de los platos por categorías directo desde la API.

![image](https://github.com/user-attachments/assets/bc9f932e-0745-4a5b-9ef6-cc46f28ceb54)

Es la función encargada de mostrar los detalles de los platos por categorías obtenidas directo desde la API.

## ExchangeRate
1. http://localhost:8000/convertir/

![image](https://github.com/user-attachments/assets/b7ba25e5-fd9e-4450-b6a9-c643b037812e)

En este apartado se pueden realizar la conversión de divisas seleccionando una moneda de origen y una de destino e ingresando la cantidad a convertir.

![image](https://github.com/user-attachments/assets/76b59bce-4da5-4f58-9f2e-ba19d48641f5)
![image](https://github.com/user-attachments/assets/2da52b33-3e96-4529-9ffb-caba2fae1259)

Formulario para poder seleccionar la moneda de origen y destino.
Se pueden añadir monedas de todos estos [países soportados](https://v6.exchangerate-api.com/v6/fc09d92b0875c138029afc21/latest/USD) por el API.

El API funciona mandando la solicitud para obtener la tasa de cambio mediante el código de la moneda, por ejemplo 'USD' que sería el Dólar Estadounidense.

![image](https://github.com/user-attachments/assets/d2953d95-978d-457d-a461-d68cedc379e0)

Función encargada de obtener las tasas de cambio de las monedas directo desde la API.

![image](https://github.com/user-attachments/assets/51e173a1-50a7-40c6-939e-78803ff0e03d)

Función encargada de convertir las monedas y mostrar el apartado de conversión de divisas.

- Ejemplo de Conversión:

![image](https://github.com/user-attachments/assets/fa69b9ac-e4ee-44b3-ae2b-744fbef38a6f)

En el ejemplo se puede visualizar como se convierte la moneda de origen USD "Dólar Estadounidense" con 100 de cantidad a la moneda de destino CLP "Peso Chileno" y se muestra en el Resultado final de 98295,74 CLP.
