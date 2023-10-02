CREATE DATABASE reunion_general;
use reunion_general;

CREATE TABLE hermanos(
	hermano_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    hora_llegada TIME DEFAULT (TIME(NOW())),
    observacion VARCHAR(255) NOT NULL
);


INSERT INTO hermanos(nombre, apellido, observacion)
VALUES ('Ana', 'Chirinos', ''),
	('Kevin', 'Serrano', 'Nuevo'),
    ('Luna', 'Pedraza', 'Viejo'),
    ('Enzo', 'Pedraza', '');