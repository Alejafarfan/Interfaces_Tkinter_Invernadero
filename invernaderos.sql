-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-05-2025 a las 04:00:11
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `invernaderos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invernaderos`
--

CREATE TABLE `invernaderos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `superficie` varchar(50) DEFAULT NULL,
  `cultivo` varchar(50) DEFAULT NULL,
  `fecha_creacion` date DEFAULT NULL,
  `responsable` varchar(100) DEFAULT NULL,
  `capacidad` varchar(50) DEFAULT NULL,
  `sistema_riego` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT 'Operativo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `invernaderos`
--

INSERT INTO `invernaderos` (`id`, `nombre`, `superficie`, `cultivo`, `fecha_creacion`, `responsable`, `capacidad`, `sistema_riego`, `estado`) VALUES
(8, 'Invernadero los Andes ', '23000 m', 'Frutas', '2014-02-05', 'Sergio Moreno', '500000', 'Por goteo', 'Operativo'),
(9, 'Invernadero las Flores ', '45000 m', 'Flores', '2018-12-23', 'Carlos Sanchez', '34000', 'Por goteo', 'Reparación'),
(10, 'Invernadero Los Pinos', '67000 m', 'Verduras', '2020-05-04', 'Samir Carvajal', '3420000', 'Automatizado', 'Inspección'),
(11, 'Invernadero El Mirador ', '76000 m', 'Verduras', '2017-04-22', 'Sandra Gomez', '453000', 'Manual', 'Expansión'),
(12, 'Invernadero Las Brisas', '34000 m', 'Verduras', '2008-03-13', 'Xavi Sanchez', '43000', 'Por goteo', 'Operativo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `usuario` varchar(50) DEFAULT NULL,
  `clave` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `clave`) VALUES
(1, 'obama', 'negro'),
(3, 'Juan', '123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `invernaderos`
--
ALTER TABLE `invernaderos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `invernaderos`
--
ALTER TABLE `invernaderos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
