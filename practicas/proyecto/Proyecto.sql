-- base de datos
CREATE DATABASE proyecto;
USE proyecto;
-- tabla : curso
CREATE TABLE curso
(
    id VARCHAR(20),
    nombre VARCHAR (20),
    tecnologia VARCHAR (20),
    costo INT(5),
    CONSTRAINT curso_id_pk PRIMARY KEY (id)
);
-- tabla : alumno
CREATE TABLE alumno
(
    rfc VARCHAR(10),
    nombre VARCHAR(30),
    id_curso VARCHAR(20),
    CONSTRAINT curso_id_pk PRIMARY KEY (rfc),
    CONSTRAINT alumno_id_fk FOREIGN KEY(id_curso)
	REFERENCES curso(id) ON DELETE SET NULL
);
-- tabla : instructor
CREATE TABLE instructor
(
    numero_empleado INT(5) AUTO_INCREMENT,
    nombre VARCHAR(30),
    tecnologia VARCHAR(20),
    id_curso VARCHAR(20),
    CONSTRAINT inst_num_pk PRIMARY KEY (numero_empleado),
	CONSTRAINT inst_id_fk FOREIGN KEY (id_curso)
	REFERENCES curso (id) ON DELETE SET NULL
    );

-- population
--      tabla : curso 
INSERT INTO `proyecto`.`curso` (`id`, `nombre`, `tecnologia`, `costo`) VALUES ('100', 'Curso 100', 'Tecnología 100', '100');
INSERT INTO `proyecto`.`curso` (`id`, `nombre`, `tecnologia`, `costo`) VALUES ('200', 'Curso 200', 'Tecnología 200', '200');
INSERT INTO `proyecto`.`curso` (`id`, `nombre`, `tecnologia`, `costo`) VALUES ('300', 'Curso 300', 'Tecnología 300', '300');
--      tabla : alumno
INSERT INTO `proyecto`.`alumno` (`rfc`, `nombre`, `id_curso`) VALUES ('RFC001', 'Nombre 001', '100');
INSERT INTO `proyecto`.`alumno` (`rfc`, `nombre`, `id_curso`) VALUES ('RFC002', 'Nombre 2', '200');
INSERT INTO `proyecto`.`alumno` (`rfc`, `nombre`, `id_curso`) VALUES ('RFC003', 'Nombre 003', '300');
--      tabla : instructor
INSERT INTO `proyecto`.`instructor` (`numero_empleado`, `nombre`, `tecnologia`, `id_curso`) VALUES ('1000', 'Instructor 100', '100', '100');
INSERT INTO `proyecto`.`instructor` (`numero_empleado`, `nombre`, `tecnologia`, `id_curso`) VALUES ('2000', 'Instructor', '200', '200');
INSERT INTO `proyecto`.`instructor` (`numero_empleado`, `nombre`, `tecnologia`, `id_curso`) VALUES ('3000', 'Instructor 3000', '300', '300');
