-- DROP DATABASE bd_productos;
CREATE DATABASE bd_productos;
USE bd_productos;


-- DROP TABLE producto;
CREATE TABLE producto (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL DEFAULT '',
  precio FLOAT UNSIGNED NOT NULL DEFAULT 0,
  cantidad_disponible INT NOT NULL DEFAULT 0,
  descripcion VARCHAR(250) NOT NULL DEFAULT '',
  fecha_creacion DATETIME NOT NULL DEFAULT NOW(),
  categoria VARCHAR(50) NOT NULL DEFAULT 'Otros',
  PRIMARY KEY(id)
);

-- DROP TABLE producto;
INSERT INTO producto (nombre, precio, cantidad_disponible, descripcion, categoria) 
VALUES ('Tutos de pollo', 3600, 32, 'Caja de pollos, incluye 32 tutos', 'Carnes');