-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla restaurantemichu.auth_group: ~0 rows (aproximadamente)

-- Volcando datos para la tabla restaurantemichu.auth_group_permissions: ~0 rows (aproximadamente)

-- Volcando datos para la tabla restaurantemichu.auth_permission: ~128 rows (aproximadamente)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add inventario principal', 7, 'add_inventarioprincipal'),
	(26, 'Can change inventario principal', 7, 'change_inventarioprincipal'),
	(27, 'Can delete inventario principal', 7, 'delete_inventarioprincipal'),
	(28, 'Can view inventario principal', 7, 'view_inventarioprincipal'),
	(29, 'Can add insumo', 8, 'add_insumo'),
	(30, 'Can change insumo', 8, 'change_insumo'),
	(31, 'Can delete insumo', 8, 'delete_insumo'),
	(32, 'Can view insumo', 8, 'view_insumo'),
	(33, 'Can add movimiento inventario', 9, 'add_movimientoinventario'),
	(34, 'Can change movimiento inventario', 9, 'change_movimientoinventario'),
	(35, 'Can delete movimiento inventario', 9, 'delete_movimientoinventario'),
	(36, 'Can view movimiento inventario', 9, 'view_movimientoinventario'),
	(37, 'Can add reporte consumo', 10, 'add_reporteconsumo'),
	(38, 'Can change reporte consumo', 10, 'change_reporteconsumo'),
	(39, 'Can delete reporte consumo', 10, 'delete_reporteconsumo'),
	(40, 'Can view reporte consumo', 10, 'view_reporteconsumo'),
	(41, 'Can add reporte inventario', 11, 'add_reporteinventario'),
	(42, 'Can change reporte inventario', 11, 'change_reporteinventario'),
	(43, 'Can delete reporte inventario', 11, 'delete_reporteinventario'),
	(44, 'Can view reporte inventario', 11, 'view_reporteinventario'),
	(45, 'Can add categoria inventario', 12, 'add_categoriainventario'),
	(46, 'Can change categoria inventario', 12, 'change_categoriainventario'),
	(47, 'Can delete categoria inventario', 12, 'delete_categoriainventario'),
	(48, 'Can view categoria inventario', 12, 'view_categoriainventario'),
	(49, 'Can add menu', 13, 'add_menu'),
	(50, 'Can change menu', 13, 'change_menu'),
	(51, 'Can delete menu', 13, 'delete_menu'),
	(52, 'Can view menu', 13, 'view_menu'),
	(53, 'Can add categoria', 14, 'add_categoria'),
	(54, 'Can change categoria', 14, 'change_categoria'),
	(55, 'Can delete categoria', 14, 'delete_categoria'),
	(56, 'Can view categoria', 14, 'view_categoria'),
	(57, 'Can add producto', 15, 'add_producto'),
	(58, 'Can change producto', 15, 'change_producto'),
	(59, 'Can delete producto', 15, 'delete_producto'),
	(60, 'Can view producto', 15, 'view_producto'),
	(61, 'Can add persona', 16, 'add_persona'),
	(62, 'Can change persona', 16, 'change_persona'),
	(63, 'Can delete persona', 16, 'delete_persona'),
	(64, 'Can view persona', 16, 'view_persona'),
	(65, 'Can add cliente', 17, 'add_cliente'),
	(66, 'Can change cliente', 17, 'change_cliente'),
	(67, 'Can delete cliente', 17, 'delete_cliente'),
	(68, 'Can view cliente', 17, 'view_cliente'),
	(69, 'Can add personal', 18, 'add_personal'),
	(70, 'Can change personal', 18, 'change_personal'),
	(71, 'Can delete personal', 18, 'delete_personal'),
	(72, 'Can view personal', 18, 'view_personal'),
	(73, 'Can add mesa', 19, 'add_mesa'),
	(74, 'Can change mesa', 19, 'change_mesa'),
	(75, 'Can delete mesa', 19, 'delete_mesa'),
	(76, 'Can view mesa', 19, 'view_mesa'),
	(77, 'Can add reserva', 20, 'add_reserva'),
	(78, 'Can change reserva', 20, 'change_reserva'),
	(79, 'Can delete reserva', 20, 'delete_reserva'),
	(80, 'Can view reserva', 20, 'view_reserva'),
	(81, 'Can add pedido', 21, 'add_pedido'),
	(82, 'Can change pedido', 21, 'change_pedido'),
	(83, 'Can delete pedido', 21, 'delete_pedido'),
	(84, 'Can view pedido', 21, 'view_pedido'),
	(85, 'Can add historial pedido', 22, 'add_historialpedido'),
	(86, 'Can change historial pedido', 22, 'change_historialpedido'),
	(87, 'Can delete historial pedido', 22, 'delete_historialpedido'),
	(88, 'Can view historial pedido', 22, 'view_historialpedido'),
	(89, 'Can add item pedido', 23, 'add_itempedido'),
	(90, 'Can change item pedido', 23, 'change_itempedido'),
	(91, 'Can delete item pedido', 23, 'delete_itempedido'),
	(92, 'Can view item pedido', 23, 'view_itempedido'),
	(93, 'Can add receta', 24, 'add_receta'),
	(94, 'Can change receta', 24, 'change_receta'),
	(95, 'Can delete receta', 24, 'delete_receta'),
	(96, 'Can view receta', 24, 'view_receta'),
	(97, 'Can add factura', 25, 'add_factura'),
	(98, 'Can change factura', 25, 'change_factura'),
	(99, 'Can delete factura', 25, 'delete_factura'),
	(100, 'Can view factura', 25, 'view_factura'),
	(101, 'Can add impuesto', 26, 'add_impuesto'),
	(102, 'Can change impuesto', 26, 'change_impuesto'),
	(103, 'Can delete impuesto', 26, 'delete_impuesto'),
	(104, 'Can view impuesto', 26, 'view_impuesto'),
	(105, 'Can add promocion', 27, 'add_promocion'),
	(106, 'Can change promocion', 27, 'change_promocion'),
	(107, 'Can delete promocion', 27, 'delete_promocion'),
	(108, 'Can view promocion', 27, 'view_promocion'),
	(109, 'Can add item factura', 28, 'add_itemfactura'),
	(110, 'Can change item factura', 28, 'change_itemfactura'),
	(111, 'Can delete item factura', 28, 'delete_itemfactura'),
	(112, 'Can view item factura', 28, 'view_itemfactura'),
	(113, 'Can add mesero', 29, 'add_mesero'),
	(114, 'Can change mesero', 29, 'change_mesero'),
	(115, 'Can delete mesero', 29, 'delete_mesero'),
	(116, 'Can view mesero', 29, 'view_mesero'),
	(117, 'Can add historial factura', 30, 'add_historialfactura'),
	(118, 'Can change historial factura', 30, 'change_historialfactura'),
	(119, 'Can delete historial factura', 30, 'delete_historialfactura'),
	(120, 'Can view historial factura', 30, 'view_historialfactura'),
	(121, 'Can add estadistica', 31, 'add_estadistica'),
	(122, 'Can change estadistica', 31, 'change_estadistica'),
	(123, 'Can delete estadistica', 31, 'delete_estadistica'),
	(124, 'Can view estadistica', 31, 'view_estadistica'),
	(125, 'Can add reporte', 32, 'add_reporte'),
	(126, 'Can change reporte', 32, 'change_reporte'),
	(127, 'Can delete reporte', 32, 'delete_reporte'),
	(128, 'Can view reporte', 32, 'view_reporte');

-- Volcando datos para la tabla restaurantemichu.auth_user: ~0 rows (aproximadamente)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$870000$jSxUgAfqYLxJ3ueBTePmNh$rT9Duq5dAgVPK0siu0lIERISkeDh87qhk3QHRDpfxA0=', '2025-02-04 13:53:06.480020', 1, 'michu', '', '', 'michu@gmail.com', 1, 1, '2025-02-04 13:19:02.443592');

-- Volcando datos para la tabla restaurantemichu.auth_user_groups: ~0 rows (aproximadamente)

-- Volcando datos para la tabla restaurantemichu.auth_user_user_permissions: ~0 rows (aproximadamente)

-- Volcando datos para la tabla restaurantemichu.django_admin_log: ~0 rows (aproximadamente)
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2025-02-04 13:58:06.591715', '1', 'Gerardo', 1, '[{"added": {}}]', 17, 1),
	(2, '2025-02-04 13:59:34.678584', '2', 'Carolina', 1, '[{"added": {}}]', 17, 1),
	(3, '2025-02-04 13:59:54.062500', '1', 'Menu1', 1, '[{"added": {}}]', 13, 1),
	(4, '2025-02-04 14:00:14.974953', '1', 'Bebidas', 1, '[{"added": {}}]', 14, 1),
	(5, '2025-02-04 14:00:31.212953', '2', 'Entradas', 1, '[{"added": {}}]', 14, 1),
	(6, '2025-02-04 14:00:39.242017', '3', 'Porciones', 1, '[{"added": {}}]', 14, 1),
	(7, '2025-02-04 14:00:44.246434', '4', 'sopas', 1, '[{"added": {}}]', 14, 1),
	(8, '2025-02-04 14:01:11.660274', '1', 'Coca-Cola', 1, '[{"added": {}}]', 15, 1),
	(9, '2025-02-04 14:02:11.628569', '2', 'papas fritas', 1, '[{"added": {}}]', 15, 1),
	(10, '2025-02-04 14:02:51.572553', '3', 'Croqueta de Atun', 1, '[{"added": {}}]', 15, 1),
	(11, '2025-02-04 14:03:17.704959', '4', 'Crema de Zanahoria', 1, '[{"added": {}}]', 15, 1),
	(12, '2025-02-04 14:03:22.131924', '4', 'Crema de Zanahoria', 2, '[{"changed": {"fields": ["Disponibilidad"]}}]', 15, 1),
	(13, '2025-02-04 14:04:00.077330', '1', 'Inventario Principal 1', 1, '[{"added": {}}]', 7, 1),
	(14, '2025-02-04 14:04:13.690747', '1', 'Abarrotes', 1, '[{"added": {}}]', 12, 1),
	(15, '2025-02-04 14:04:19.523060', '2', 'Hortalizas', 1, '[{"added": {}}]', 12, 1),
	(16, '2025-02-04 14:04:24.977114', '3', 'Verduras', 1, '[{"added": {}}]', 12, 1),
	(17, '2025-02-04 14:04:57.341955', '1', 'Zanahoria (0 unidades)', 1, '[{"added": {}}]', 8, 1),
	(18, '2025-02-04 14:05:25.101674', '2', 'papa (0 libras)', 1, '[{"added": {}}]', 8, 1),
	(19, '2025-02-04 14:06:23.426283', '3', 'Arroz (0 onzas)', 1, '[{"added": {}}]', 8, 1),
	(20, '2025-02-04 14:06:57.823832', '4', 'frutas', 1, '[{"added": {}}]', 12, 1),
	(21, '2025-02-04 14:07:22.950684', '4', 'Azucar (0 gramos)', 1, '[{"added": {}}]', 8, 1),
	(22, '2025-02-04 14:08:00.836269', '1', 'Entrada - Zanahoria (20 unidades)', 1, '[{"added": {}}]', 9, 1),
	(23, '2025-02-04 14:08:13.691146', '2', 'Entrada - papa (20 libras)', 1, '[{"added": {}}]', 9, 1),
	(24, '2025-02-04 14:08:25.785649', '3', 'Entrada - Arroz (50 onzas)', 1, '[{"added": {}}]', 9, 1),
	(25, '2025-02-04 14:08:46.666680', '4', 'Entrada - Azucar (6000 gramos)', 1, '[{"added": {}}]', 9, 1),
	(26, '2025-02-04 14:09:00.391058', '1', 'Zanahoria: 0 unidades (2025-02-04 - 2025-02-04)', 1, '[{"added": {}}]', 10, 1),
	(27, '2025-02-04 14:09:11.853101', '1', 'Reporte de Inventario - Inventario Principal 1 (2025-02-04 14:09:11.849929+00:00)', 1, '[{"added": {}}]', 11, 1),
	(28, '2025-02-04 14:09:19.050986', '1', 'Reporte de Inventario - Inventario Principal 1 (2025-02-04 14:09:11.849929+00:00)', 2, '[]', 11, 1),
	(29, '2025-02-04 14:10:49.678172', '5', 'mariscos', 1, '[{"added": {}}]', 12, 1),
	(30, '2025-02-04 14:10:58.652635', '5', 'atun (0 gramos)', 1, '[{"added": {}}]', 8, 1),
	(31, '2025-02-04 14:11:30.016590', '5', 'Entrada - atun (5000 gramos)', 1, '[{"added": {}}]', 9, 1),
	(32, '2025-02-04 14:11:55.997077', '1', 'Crema de Zanahoria - Zanahoria: 2 unidades', 1, '[{"added": {}}]', 24, 1),
	(33, '2025-02-04 14:12:10.401816', '2', 'Croqueta de Atun - atun: 120 gramos', 1, '[{"added": {}}]', 24, 1),
	(34, '2025-02-04 14:12:24.632869', '3', 'papas fritas - papa: 2 libras', 1, '[{"added": {}}]', 24, 1),
	(35, '2025-02-04 14:13:18.195761', '1', 'P001', 1, '[{"added": {}}, {"added": {"name": "item pedido", "object": "P001 - Croqueta de Atun"}}, {"added": {"name": "item pedido", "object": "P001 - Crema de Zanahoria"}}]', 21, 1),
	(36, '2025-02-04 14:14:44.964830', '1', 'IVA', 1, '[{"added": {}}]', 26, 1),
	(37, '2025-02-04 14:15:12.302710', '3', 'Cristina', 1, '[{"added": {}}]', 29, 1),
	(38, '2025-02-04 14:15:42.921817', '1', 'Mesa M111 - Capacidad 5', 1, '[{"added": {}}]', 19, 1),
	(39, '2025-02-04 14:15:44.566930', '1', 'F001', 1, '[{"added": {}}]', 25, 1),
	(40, '2025-02-04 14:16:22.828507', '1', 'F001', 2, '[]', 25, 1),
	(41, '2025-02-04 14:16:40.437315', '1', 'P001', 2, '[]', 21, 1),
	(42, '2025-02-04 14:18:41.251774', '2', 'P002', 1, '[{"added": {}}, {"added": {"name": "item pedido", "object": "P002 - Coca-Cola"}}, {"added": {"name": "item pedido", "object": "P002 - papas fritas"}}]', 21, 1),
	(43, '2025-02-04 14:19:17.771432', '1', 'Descuento por Martes loco', 1, '[{"added": {}}]', 27, 1),
	(44, '2025-02-04 14:19:52.033671', '4', 'Joel', 1, '[{"added": {}}]', 29, 1),
	(45, '2025-02-04 14:20:12.884900', '2', 'Mesa M112 - Capacidad 10', 1, '[{"added": {}}]', 19, 1),
	(46, '2025-02-04 14:20:14.826957', '2', 'F002', 1, '[{"added": {}}]', 25, 1),
	(47, '2025-02-04 14:20:56.231751', '2', 'P002', 2, '[{"changed": {"fields": ["Estado"]}}]', 21, 1),
	(48, '2025-02-04 14:21:54.835103', '3', 'P003', 1, '[{"added": {}}, {"added": {"name": "item pedido", "object": "P003 - Crema de Zanahoria"}}]', 21, 1),
	(49, '2025-02-04 14:23:01.477944', '3', 'F003', 1, '[{"added": {}}]', 25, 1),
	(50, '2025-02-04 14:23:18.858207', '3', 'P003', 2, '[{"changed": {"fields": ["Estado"]}}]', 21, 1),
	(51, '2025-02-04 14:23:41.017059', '1', 'Estadisticas martes 4 de febrero (2025-02-04 - 2025-02-04)', 1, '[{"added": {}}]', 31, 1),
	(52, '2025-02-04 14:23:53.367714', '1', 'Reporte object (1)', 1, '[{"added": {}}]', 32, 1),
	(53, '2025-02-04 14:32:02.155660', '1', 'Historial desde 2025-02-04 hasta 2025-02-04', 1, '[{"added": {}}]', 30, 1),
	(54, '2025-02-04 14:33:45.499729', '1', 'Gerardo - 2025-02-04', 1, '[{"added": {}}]', 20, 1),
	(55, '2025-02-04 14:35:28.753242', '2', 'Carolina - 2025-02-04', 1, '[{"added": {}}]', 20, 1),
	(56, '2025-02-04 14:37:13.307032', '3', 'Mesa M113 - Capacidad 7', 1, '[{"added": {}}]', 19, 1),
	(57, '2025-02-04 14:37:32.358327', '4', 'Mesa M114 - Capacidad 8', 1, '[{"added": {}}]', 19, 1),
	(58, '2025-02-04 14:39:22.912230', '4', 'P004', 1, '[{"added": {}}, {"added": {"name": "item pedido", "object": "P004 - papas fritas"}}, {"added": {"name": "item pedido", "object": "P004 - Coca-Cola"}}]', 21, 1),
	(59, '2025-02-04 14:39:46.605324', '5', 'P005', 1, '[{"added": {}}, {"added": {"name": "item pedido", "object": "P005 - Croqueta de Atun"}}]', 21, 1),
	(60, '2025-02-04 14:40:18.892994', '4', 'F004', 1, '[{"added": {}}]', 25, 1),
	(61, '2025-02-04 14:40:56.628689', '5', 'P005', 1, '[{"added": {}}]', 25, 1),
	(62, '2025-02-04 14:41:18.330837', '4', 'P004', 2, '[{"changed": {"fields": ["Estado"]}}]', 21, 1),
	(63, '2025-02-04 14:41:29.189474', '5', 'P005', 2, '[{"changed": {"fields": ["Estado"]}}]', 21, 1);

-- Volcando datos para la tabla restaurantemichu.django_content_type: ~32 rows (aproximadamente)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(31, 'estadisticas', 'estadistica'),
	(32, 'estadisticas', 'reporte'),
	(25, 'facturacion', 'factura'),
	(30, 'facturacion', 'historialfactura'),
	(26, 'facturacion', 'impuesto'),
	(28, 'facturacion', 'itemfactura'),
	(29, 'facturacion', 'mesero'),
	(27, 'facturacion', 'promocion'),
	(12, 'inventario', 'categoriainventario'),
	(8, 'inventario', 'insumo'),
	(7, 'inventario', 'inventarioprincipal'),
	(9, 'inventario', 'movimientoinventario'),
	(10, 'inventario', 'reporteconsumo'),
	(11, 'inventario', 'reporteinventario'),
	(14, 'menu', 'categoria'),
	(13, 'menu', 'menu'),
	(15, 'menu', 'producto'),
	(17, 'mesas', 'cliente'),
	(19, 'mesas', 'mesa'),
	(16, 'mesas', 'persona'),
	(18, 'mesas', 'personal'),
	(20, 'mesas', 'reserva'),
	(22, 'pedidos', 'historialpedido'),
	(23, 'pedidos', 'itempedido'),
	(21, 'pedidos', 'pedido'),
	(24, 'pedidos', 'receta'),
	(6, 'sessions', 'session');

-- Volcando datos para la tabla restaurantemichu.django_migrations: ~42 rows (aproximadamente)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2025-02-04 13:17:32.064765'),
	(2, 'auth', '0001_initial', '2025-02-04 13:17:32.971084'),
	(3, 'admin', '0001_initial', '2025-02-04 13:17:33.233002'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2025-02-04 13:17:33.242241'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-04 13:17:33.252180'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2025-02-04 13:17:33.367647'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2025-02-04 13:17:33.483911'),
	(8, 'auth', '0003_alter_user_email_max_length', '2025-02-04 13:17:33.517463'),
	(9, 'auth', '0004_alter_user_username_opts', '2025-02-04 13:17:33.529067'),
	(10, 'auth', '0005_alter_user_last_login_null', '2025-02-04 13:17:33.616674'),
	(11, 'auth', '0006_require_contenttypes_0002', '2025-02-04 13:17:33.619174'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2025-02-04 13:17:33.630874'),
	(13, 'auth', '0008_alter_user_username_max_length', '2025-02-04 13:17:33.740581'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2025-02-04 13:17:33.815631'),
	(15, 'auth', '0010_alter_group_name_max_length', '2025-02-04 13:17:33.861177'),
	(16, 'auth', '0011_update_proxy_permissions', '2025-02-04 13:17:33.871995'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2025-02-04 13:17:33.989186'),
	(18, 'estadisticas', '0001_initial', '2025-02-04 13:17:34.023998'),
	(19, 'estadisticas', '0002_alter_estadistica_ventas_totales', '2025-02-04 13:17:34.062910'),
	(20, 'mesas', '0001_initial', '2025-02-04 13:17:34.690199'),
	(21, 'mesas', '0002_remove_cliente_activo', '2025-02-04 13:17:34.742581'),
	(22, 'mesas', '0003_alter_reserva_cliente', '2025-02-04 13:17:34.937203'),
	(23, 'mesas', '0004_remove_mesa_identificador_mesa_cantidad_uso_and_more', '2025-02-04 13:17:35.177432'),
	(24, 'pedidos', '0001_initial', '2025-02-04 13:17:35.799286'),
	(25, 'pedidos', '0002_alter_pedido_cliente_and_more', '2025-02-04 13:17:36.271480'),
	(26, 'pedidos', '0003_alter_pedido_cliente_and_more', '2025-02-04 13:17:36.585993'),
	(27, 'menu', '0001_initial', '2025-02-04 13:17:36.839012'),
	(28, 'pedidos', '0004_alter_detallepedido_producto_and_more', '2025-02-04 13:17:37.160202'),
	(29, 'pedidos', '0005_remove_pedido_reservacion_pedido_reserva_and_more', '2025-02-04 13:17:37.388651'),
	(30, 'pedidos', '0006_alter_pedido_mesa_delete_mesa', '2025-02-04 13:17:37.527906'),
	(31, 'pedidos', '0007_alter_pedido_cliente', '2025-02-04 13:17:37.721810'),
	(32, 'pedidos', '0008_pedido_codigo', '2025-02-04 13:17:37.812726'),
	(33, 'menu', '0002_producto_cantidad_vendida', '2025-02-04 13:17:37.852097'),
	(34, 'facturacion', '0001_initial', '2025-02-04 13:17:39.496662'),
	(35, 'facturacion', '0002_mesero_alter_pedido_cliente_and_more', '2025-02-04 13:17:40.157987'),
	(36, 'facturacion', '0003_remove_pedido_productos_remove_pedido_cliente_and_more', '2025-02-04 13:17:40.788840'),
	(37, 'facturacion', '0004_factura_mesa_factura_mesero', '2025-02-04 13:17:41.142549'),
	(38, 'facturacion', '0005_remove_factura_metodo_pago_efectivo_and_more', '2025-02-04 13:17:42.050526'),
	(39, 'facturacion', '0006_alter_factura_monto_recibido', '2025-02-04 13:17:42.065371'),
	(40, 'facturacion', '0007_alter_factura_cambio_alter_factura_descuento_and_more', '2025-02-04 13:17:42.904421'),
	(41, 'facturacion', '0008_alter_impuesto_porcentaje_alter_itemfactura_subtotal_and_more', '2025-02-04 13:17:43.083662'),
	(42, 'facturacion', '0009_alter_factura_cambio_alter_factura_descuento_and_more', '2025-02-04 13:17:44.101242'),
	(43, 'facturacion', '0010_alter_factura_cambio_alter_factura_descuento_and_more', '2025-02-04 13:17:45.093042'),
	(44, 'facturacion', '0011_facturahistorial_historialfactura_and_more', '2025-02-04 13:17:45.334360'),
	(45, 'facturacion', '0012_remove_historialfactura_facturas_and_more', '2025-02-04 13:17:45.369739'),
	(46, 'facturacion', '0013_alter_itemfactura_options_alter_promocion_options', '2025-02-04 13:17:45.379331'),
	(47, 'facturacion', '0014_alter_itemfactura_factura', '2025-02-04 13:17:45.393024'),
	(48, 'inventario', '0001_initial', '2025-02-04 13:17:45.573077'),
	(49, 'inventario', '0002_inventarioprincipal_remove_categoria_menu_and_more', '2025-02-04 13:17:46.447359'),
	(50, 'inventario', '0003_rename_categoria_categoriainventario_and_more', '2025-02-04 13:17:46.666896'),
	(51, 'inventario', '0004_alter_insumo_cantidad_disponible', '2025-02-04 13:17:46.846639'),
	(52, 'inventario', '0005_alter_movimientoinventario_cantidad', '2025-02-04 13:17:46.915880'),
	(53, 'inventario', '0006_alter_categoriainventario_options_and_more', '2025-02-04 13:17:46.938139'),
	(54, 'menu', '0003_alter_producto_precio', '2025-02-04 13:17:46.947803'),
	(55, 'mesas', '0005_remove_personal_rol_and_more', '2025-02-04 13:17:47.042922'),
	(56, 'mesas', '0006_alter_personal_options', '2025-02-04 13:17:47.048438'),
	(57, 'mesas', '0007_remove_persona_email_and_more', '2025-02-04 13:17:47.251240'),
	(58, 'pedidos', '0009_remove_pedido_actualizado_en_remove_pedido_creado_en_and_more', '2025-02-04 13:17:48.036769'),
	(59, 'pedidos', '0010_receta', '2025-02-04 13:17:48.251150'),
	(60, 'pedidos', '0011_alter_receta_cantidad_necesaria', '2025-02-04 13:17:48.338506'),
	(61, 'pedidos', '0012_alter_historialpedido_options', '2025-02-04 13:17:48.344474'),
	(62, 'sessions', '0001_initial', '2025-02-04 13:17:48.383375');

-- Volcando datos para la tabla restaurantemichu.django_session: ~0 rows (aproximadamente)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('0g87gfsxfx69kzpp0o2vz1gq9unnei1z', '.eJxVjMEOwiAQRP-FsyGwdV3w6N1vaGDZStVAUtqT8d-VpAc9zGXem3mpMWxrHrcmyzgndVZWHX67GPghpYN0D-VWNdeyLnPUXdE7bfpakzwvu_t3kEPLfc1onHUMHsRIAibkSYjEBEALA0EUcJ5wciY5wsGhHNEb8fYbOqn3B9YvNv4:1tfJMQ:dlx1VvnNzeiR-WcHMXDAEDDIC0NZdt32_2zPRW2bvw0', '2025-02-18 13:53:06.482681'),
	('lg3s3sevnlkoiio3lrercufanh4kwx45', '.eJxVjMEOwiAQRP-FsyGwdV3w6N1vaGDZStVAUtqT8d-VpAc9zGXem3mpMWxrHrcmyzgndVZWHX67GPghpYN0D-VWNdeyLnPUXdE7bfpakzwvu_t3kEPLfc1onHUMHsRIAibkSYjEBEALA0EUcJ5wciY5wsGhHNEb8fYbOqn3B9YvNv4:1tfJGI:DqK4Ix6CrTkJrzJDVXI_PlLIbNzH_pAP_bP15anrjSk', '2025-02-18 13:46:46.296596'),
	('wr9iih34bz8c1qfqr5rq5a3l530mfa5r', '.eJxVjMEOwiAQRP-FsyGwdV3w6N1vaGDZStVAUtqT8d-VpAc9zGXem3mpMWxrHrcmyzgndVZWHX67GPghpYN0D-VWNdeyLnPUXdE7bfpakzwvu_t3kEPLfc1onHUMHsRIAibkSYjEBEALA0EUcJ5wciY5wsGhHNEb8fYbOqn3B9YvNv4:1tfIpj:pUHa1_Mz2msSXvDGZd4qy8hKkTUJOvt4u_1isiI8FkE', '2025-02-18 13:19:19.653279');

-- Volcando datos para la tabla restaurantemichu.estadisticas_estadistica: ~0 rows (aproximadamente)
INSERT INTO `estadisticas_estadistica` (`id`, `titulo`, `fecha_inicio`, `fecha_fin`, `mejor_mesero`, `mesa_mas_usada`, `producto_mas_vendido`, `ventas_totales`) VALUES
	(1, 'Estadisticas martes 4 de febrero', '2025-02-04', '2025-02-04', 'Cristina', 'M111', 'Crema de Zanahoria', 33.06);

-- Volcando datos para la tabla restaurantemichu.estadisticas_reporte: ~0 rows (aproximadamente)
INSERT INTO `estadisticas_reporte` (`id`, `titulo`, `fecha_inicio`, `fecha_fin`) VALUES
	(1, 'Estadisticas martes 4 de febrero', '2025-02-04', '2025-02-04');

-- Volcando datos para la tabla restaurantemichu.facturacion_factura: ~0 rows (aproximadamente)
INSERT INTO `facturacion_factura` (`numero`, `codigo`, `total`, `subtotal`, `impuesto_total`, `descuento`, `fecha`, `impuesto_id`, `pedido_id`, `promocion_id`, `mesa_id`, `mesero_id`, `cambio`, `metodo_pago`, `monto_recibido`, `recargo_tarjeta`, `referencia_transferencia`) VALUES
	(1, 'F001', 11.50, 10.00, 1.50, 0.00, '2025-02-04', 1, 1, NULL, 1, 3, 8.50, 'EFECTIVO', 20.00, 0.00, NULL),
	(2, 'F002', 7.81, 7.10, 1.06, 0.35, '2025-02-04', 1, 2, 1, 2, 4, 22.19, 'EFECTIVO', 30.00, 0.00, NULL),
	(3, 'F003', 13.75, 12.50, 1.88, 0.63, '2025-02-04', 1, 3, 1, 1, 3, 6.25, 'EFECTIVO', 20.00, 0.00, NULL),
	(4, 'F004', 7.81, 7.10, 1.06, 0.35, '2025-02-04', 1, 4, 1, 3, 3, 7.19, 'EFECTIVO', 15.00, 0.00, NULL),
	(5, 'P005', 5.50, 5.00, 0.75, 0.25, '2025-02-04', 1, 5, 1, 4, 3, 14.50, 'EFECTIVO', 20.00, 0.00, NULL);

-- Volcando datos para la tabla restaurantemichu.facturacion_historialfactura: ~0 rows (aproximadamente)
INSERT INTO `facturacion_historialfactura` (`id`, `fecha_inicio`, `fecha_fin`) VALUES
	(1, '2025-02-04', '2025-02-04');

-- Volcando datos para la tabla restaurantemichu.facturacion_impuesto: ~0 rows (aproximadamente)
INSERT INTO `facturacion_impuesto` (`id`, `nombre`, `porcentaje`, `descripcion`) VALUES
	(1, 'IVA', 15.00, 'Impuesto al Valor Agregado');

-- Volcando datos para la tabla restaurantemichu.facturacion_itemfactura: ~0 rows (aproximadamente)
INSERT INTO `facturacion_itemfactura` (`id`, `cantidad`, `subtotal`, `factura_id`, `producto_id`) VALUES
	(1, 2, 5.00, 1, 3),
	(2, 2, 5.00, 1, 4),
	(3, 2, 5.00, 1, 3),
	(4, 2, 5.00, 1, 4),
	(5, 2, 2.60, 2, 1),
	(6, 3, 4.50, 2, 2),
	(7, 5, 12.50, 3, 4),
	(8, 3, 4.50, 4, 2),
	(9, 2, 2.60, 4, 1),
	(10, 2, 5.00, 5, 3);

-- Volcando datos para la tabla restaurantemichu.facturacion_mesero: ~0 rows (aproximadamente)
INSERT INTO `facturacion_mesero` (`persona_ptr_id`, `pedidosAtendidos`) VALUES
	(3, 0),
	(4, 0);

-- Volcando datos para la tabla restaurantemichu.facturacion_promocion: ~0 rows (aproximadamente)
INSERT INTO `facturacion_promocion` (`id`, `descripcion`, `porcentaje_descuento`) VALUES
	(1, 'Descuento por Martes loco', 5.00);

-- Volcando datos para la tabla restaurantemichu.inventario_categoriainventario: ~0 rows (aproximadamente)
INSERT INTO `inventario_categoriainventario` (`id`, `nombre`, `inventario_id`) VALUES
	(1, 'Abarrotes', 1),
	(2, 'Hortalizas', 1),
	(3, 'Verduras', 1),
	(4, 'frutas', 1),
	(5, 'mariscos', 1);

-- Volcando datos para la tabla restaurantemichu.inventario_insumo: ~0 rows (aproximadamente)
INSERT INTO `inventario_insumo` (`id`, `nombre`, `cantidad_disponible`, `unidad_medida`, `nivel_reorden`, `categoria_id`) VALUES
	(1, 'Zanahoria', 6, 'unidades', 10, 3),
	(2, 'papa', 8, 'libras', 10, 2),
	(3, 'Arroz', 50, 'onzas', 20, 1),
	(4, 'Azucar', 6000, 'gramos', 2000, 1),
	(5, 'atun', 4520, 'gramos', 500, 5);

-- Volcando datos para la tabla restaurantemichu.inventario_inventarioprincipal: ~0 rows (aproximadamente)
INSERT INTO `inventario_inventarioprincipal` (`id`, `nombre`) VALUES
	(1, 'Inventario Principal 1');

-- Volcando datos para la tabla restaurantemichu.inventario_movimientoinventario: ~0 rows (aproximadamente)
INSERT INTO `inventario_movimientoinventario` (`id`, `tipo`, `cantidad`, `fecha`, `descripcion`, `insumo_id`) VALUES
	(1, 'entrada', 20.00, '2025-02-04 14:08:00.831183', 'compra de zanahorias', 1),
	(2, 'entrada', 20.00, '2025-02-04 14:08:13.689456', 'Compra de papas', 2),
	(3, 'entrada', 50.00, '2025-02-04 14:08:25.783854', 'Compra de arroz', 3),
	(4, 'entrada', 6000.00, '2025-02-04 14:08:46.664104', 'Compra de arroz', 4),
	(5, 'entrada', 5000.00, '2025-02-04 14:11:30.015458', 'Compra de atún', 5),
	(6, 'salida', 240.00, '2025-02-04 14:16:40.427543', 'Salida por producción de Croqueta de Atun en pedido P001', 5),
	(7, 'salida', 4.00, '2025-02-04 14:16:40.434175', 'Salida por producción de Crema de Zanahoria en pedido P001', 1),
	(8, 'salida', 6.00, '2025-02-04 14:20:56.229173', 'Salida por producción de papas fritas en pedido P002', 2),
	(9, 'salida', 10.00, '2025-02-04 14:23:18.855180', 'Salida por producción de Crema de Zanahoria en pedido P003', 1),
	(10, 'salida', 6.00, '2025-02-04 14:41:18.327677', 'Salida por producción de papas fritas en pedido P004', 2),
	(11, 'salida', 240.00, '2025-02-04 14:41:29.186418', 'Salida por producción de Croqueta de Atun en pedido P005', 5);

-- Volcando datos para la tabla restaurantemichu.inventario_reporteconsumo: ~0 rows (aproximadamente)
INSERT INTO `inventario_reporteconsumo` (`id`, `fecha_inicio`, `fecha_fin`, `insumo_id`) VALUES
	(1, '2025-02-04', '2025-02-04', 1),
	(2, '2025-02-01', '2025-02-28', 5),
	(3, '2025-02-01', '2025-02-28', 1),
	(4, '2025-02-01', '2025-02-28', 2);

-- Volcando datos para la tabla restaurantemichu.inventario_reporteinventario: ~0 rows (aproximadamente)
INSERT INTO `inventario_reporteinventario` (`id`, `fecha_generacion`, `inventario_id`) VALUES
	(1, '2025-02-04 14:09:11.849929', 1);

-- Volcando datos para la tabla restaurantemichu.menu_categoria: ~0 rows (aproximadamente)
INSERT INTO `menu_categoria` (`id`, `nombre`, `menu_id`) VALUES
	(1, 'Bebidas', 1),
	(2, 'Entradas', 1),
	(3, 'Porciones', 1),
	(4, 'sopas', 1);

-- Volcando datos para la tabla restaurantemichu.menu_menu: ~0 rows (aproximadamente)
INSERT INTO `menu_menu` (`id`, `nombre`, `estado`) VALUES
	(1, 'Menu1', 1);

-- Volcando datos para la tabla restaurantemichu.menu_producto: ~0 rows (aproximadamente)
INSERT INTO `menu_producto` (`id`, `nombre`, `descripcion`, `precio`, `disponibilidad`, `categoria_id`, `cantidad_vendida`) VALUES
	(1, 'Coca-Cola', 'Coca-Cola de litro', 1.3, 1, 1, 0),
	(2, 'papas fritas', 'porcion de papas fritas', 1.5, 1, 3, 0),
	(3, 'Croqueta de Atun', 'Croqueta de Atun y papas', 2.5, 1, 2, 0),
	(4, 'Crema de Zanahoria', 'Crema de Zanahoria con jugo', 2.5, 1, 4, 0);

-- Volcando datos para la tabla restaurantemichu.mesas_cliente: ~0 rows (aproximadamente)
INSERT INTO `mesas_cliente` (`persona_ptr_id`) VALUES
	(1),
	(2);

-- Volcando datos para la tabla restaurantemichu.mesas_mesa: ~0 rows (aproximadamente)
INSERT INTO `mesas_mesa` (`id`, `numero_asientos`, `ubicacion`, `estado`, `hora_disponible`, `cantidad_uso`, `codigo`) VALUES
	(1, 5, 'Centro', 'LIBRE', '2025-02-04 23:00:00.000000', 0, 'M111'),
	(2, 10, 'Centro', 'LIBRE', '2025-02-04 14:20:10.000000', 0, 'M112'),
	(3, 7, 'Centro', 'LIBRE', '2025-02-04 14:37:12.000000', 0, 'M113'),
	(4, 8, 'Centro', 'LIBRE', '2025-02-04 14:37:30.000000', 0, 'M114');

-- Volcando datos para la tabla restaurantemichu.mesas_mesa_mesas_unidas: ~0 rows (aproximadamente)

-- Volcando datos para la tabla restaurantemichu.mesas_persona: ~0 rows (aproximadamente)
INSERT INTO `mesas_persona` (`id`, `nombre`, `apellido`, `cedula`, `telefono`) VALUES
	(1, 'Gerardo', 'Naula', '1120529645', '0987459657'),
	(2, 'Carolina', 'Ojeda', '0720547890', '0987458512'),
	(3, 'Cristina', 'Aguilar', '0780547896', '0965874512'),
	(4, 'Joel', 'Sarango', '0785458796', '0974568512');

-- Volcando datos para la tabla restaurantemichu.mesas_personal: ~0 rows (aproximadamente)

-- Volcando datos para la tabla restaurantemichu.mesas_reserva: ~0 rows (aproximadamente)
INSERT INTO `mesas_reserva` (`id`, `identificador`, `cantidad_personas`, `fecha_reserva`, `estado`, `mesa_id`, `cliente_id`) VALUES
	(1, 'R111', 2, '2025-02-04', 'CONFIRMADA', 1, 1),
	(2, 'R112', 5, '2025-02-04', 'ENCURSO', 2, 2);

-- Volcando datos para la tabla restaurantemichu.pedidos_historialpedido: ~0 rows (aproximadamente)

-- Volcando datos para la tabla restaurantemichu.pedidos_itempedido: ~0 rows (aproximadamente)
INSERT INTO `pedidos_itempedido` (`id`, `cantidad`, `precio_unitario`, `pedido_id`, `producto_id`) VALUES
	(1, 2, 2.5, 1, 3),
	(2, 2, 2.5, 1, 4),
	(3, 2, 1.3, 2, 1),
	(4, 3, 1.5, 2, 2),
	(5, 5, 2.5, 3, 4),
	(6, 3, 1.5, 4, 2),
	(7, 2, 1.3, 4, 1),
	(8, 2, 2.5, 5, 3);

-- Volcando datos para la tabla restaurantemichu.pedidos_pedido: ~0 rows (aproximadamente)
INSERT INTO `pedidos_pedido` (`id`, `cliente_id`, `estado`, `codigo`, `fecha`) VALUES
	(1, 2, 'COMPLETADO', 'P001', '2025-02-04'),
	(2, 1, 'COMPLETADO', 'P002', '2025-02-04'),
	(3, 2, 'COMPLETADO', 'P003', '2025-02-04'),
	(4, 1, 'COMPLETADO', 'P004', '2025-02-04'),
	(5, 2, 'COMPLETADO', 'P005', '2025-02-04');

-- Volcando datos para la tabla restaurantemichu.pedidos_receta: ~0 rows (aproximadamente)
INSERT INTO `pedidos_receta` (`id`, `cantidad_necesaria`, `insumo_id`, `producto_id`) VALUES
	(1, 2.00, 1, 4),
	(2, 120.00, 5, 3),
	(3, 2.00, 2, 2);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
