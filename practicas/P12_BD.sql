-- base de datos
CREATE DATABASE pruebas;
USE pruebas;
-- tabla : libro
CREATE TABLE libro
(
    id INT(5),
    titulo VARCHAR (20),
    autor VARCHAR (20),
    paginas INT(5),
    CONSTRAINT libro_id_pk PRIMARY KEY (id)
);

-- population
--      tabla : libro 
INSERT INTO `pruebas`.`libro` (`id`, `titulo`, `autor`, `paginas`) VALUES (1, 'Título 1', 'Autor 1', '100');
INSERT INTO `pruebas`.`libro` (`id`, `titulo`, `autor`, `paginas`) VALUES (2, 'Título 2', 'Autor 2', '200');
INSERT INTO `pruebas`.`libro` (`id`, `titulo`, `autor`, `paginas`) VALUES (3, 'Título 3', 'Autor 3', '300');