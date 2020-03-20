# PRÁCTICA 8
# Desde una base de datos personalizada realizar las operaciones básicas, inserción, consulta, actualización y borrado
# Tomar en cuenta los siguientes puntos:
#    * Menú de opciones para las operaciones
#    * Una opción por operación básica
#    * Opción de salida del programa

# -*- coding: utf-8 -*-
# pip install mysql-connector-python
# P12_DB.sql for MySQL Schema and data
import mysql.connector
import os
import time
import random
import sys

salir = False
ANCHO = 80
PAUSA = 2
accion = "R"
NOMBRE_APP = "PocPythonCRUD"
LINEA_INICIAL = "|" + ("=" * ANCHO) + "|"
LINEA_FINAL = "|" + ("=" * ANCHO) + "|"
LINEA_VACIA = "|" + (" " * ANCHO) + "|"
LINEA_SEPARADOR = "|" + ("-" * ANCHO) + "|"


class Libro():
    def __init__(self, id=0, titulo="Sin Título", autor="Sin Autor", paginas=0):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getPaginas(self):
        return self.paginas

    def setPaginas(self, paginas):
        self.paginas = paginas

    def toString(self):
        return "{{id:{}, título={}, autor={}, páginas={}}}".format(self.getId(), self.getTitulo(), self.getAutor(), self.getPaginas())


def limpiaPantalla():
    """Limpia la pantalla"""
    os.system('cls')


def dibujaPantallaTrabajo(libros=None):
    """Dibuja la pantalla principal (Inicial/Final)"""
    limpiaPantalla()
    print(LINEA_INICIAL)
    print("|| "+(NOMBRE_APP).rjust(ANCHO-4)+" ||")
    print(LINEA_SEPARADOR)
    print("|[{:_^8}] {:_^26} | {:_^26} | {:_^9} ||".format(
        "id", "TÍTULO", "AUTOR", "PÁGINAS"))

    for libro in libros:
        renglon = "|[{: ^8}] {: ^26} | {: ^26} | {: ^9} ||".format(
            libro.getId(), libro.getTitulo(), libro.getAutor(), libro.getPaginas())
        print(renglon)

    print(LINEA_SEPARADOR)
    dibujaMenu()


def dibujaMenu(sigInstruccionMsg=None):
    print(
        "||"+("   [C]reate  |  [R]etrieve  |  [U]pdate  |  [D]elete      |     [x] salir ").center(ANCHO-3)+" ||")
    print(LINEA_FINAL)
    if(sigInstruccionMsg):
        print(sigInstruccionMsg)


def dibujaPantallaCreate(libro=None):
    """Dibuja la pantalla principal (Inicial/Final)"""
    limpiaPantalla()
    print(LINEA_INICIAL)
    print("|| "+(NOMBRE_APP).rjust(ANCHO-4)+" ||")
    print(LINEA_SEPARADOR)
    #print("|[{:_^8}] {:_^26} | {:_^26} | {:_^9} ||".format("id", "TÍTULO", "AUTOR", "PÁGINAS"))
    print("id: " + (str)(libro.getId()))
    print("título: " + libro.getTitulo())
    print("autor: " + libro.getAutor())
    print("páginas: " + (str)(libro.getPaginas()))

    print(LINEA_SEPARADOR)
    dibujaMenu()


def dibujaPantallaActualiza(libro=None):
    """Dibuja la pantalla principal (Inicial/Final)"""
    limpiaPantalla()
    print(LINEA_INICIAL)
    print("|| "+(NOMBRE_APP).rjust(ANCHO-4)+" ||")
    print(LINEA_SEPARADOR)
    #print("|[{:_^8}] {:_^26} | {:_^26} | {:_^9} ||".format("id", "TÍTULO", "AUTOR", "PÁGINAS"))
    print("id: " + (str)(libro.getId()))
    print("título: " + libro.getTitulo())
    print("autor: " + libro.getAutor())
    print("páginas: " + (str)(libro.getPaginas()))
    print(LINEA_SEPARADOR)
    dibujaMenu()


def dibujaPantallaPrincial(mensaje):
    """Dibuja la pantalla principal (Inicial/Final)"""
    limpiaPantalla()
    print(LINEA_INICIAL)
    print("|"+("/"*60).center(ANCHO)+"|")
    print(LINEA_SEPARADOR)
    print(LINEA_VACIA)
    print(LINEA_VACIA)
    print("|" + (mensaje.center(ANCHO)) + "|")
    print(LINEA_VACIA)
    print(LINEA_VACIA)
    print(LINEA_SEPARADOR)
    print("|"+("/"*60).center(ANCHO)+"|")
    print(LINEA_FINAL)


def imprimeBienvenida():
    """Imprime el mensaje de bienvenida del sistema"""
    dibujaPantallaPrincial("B I E N V E N I D O  A  " + NOMBRE_APP)
    time.sleep(PAUSA)


def imprimeDespedida():
    """Imprime el mensaje de despedida del sistema"""
    dibujaPantallaPrincial("H A S T A   L A   V I S T A")
    time.sleep(PAUSA)


def getCxn():
    return mysql.connector.connect(host="localhost", user="root", passwd="Welcome1", db="pruebas")


def cierraCxn(cxn):
    cxn.close()


def obtenLibros():
    cxn = getCxn()
    libros = []
    try:
        cursor = cxn.cursor()
        sql = "SELECT * FROM libro"
        number_of_rows = cursor.execute(sql)
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            l = Libro(row[0], row[1], row[2], row[3])
            libros.append(l)
        cxn.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # print(e)
    finally:
        return libros


def obtenLibro(id):
    cxn = getCxn()
    libro = Libro()
    try:
        cursor = cxn.cursor()
        sql = "SELECT * FROM libro WHERE id=%s"
        number_of_rows = cursor.execute(sql, (id,))
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            libro = Libro(row[0], row[1], row[2], row[3])
        cxn.commit()
    except:
        print("Unexpected error:", sys.exc_info())
        # print(e)
    finally:
        cxn.close()
        return libro


def obtenSigId(cxn):
    # SELECT * FROM pruebas.libro ORDER BY id DESC;
    id = random.randrange(100, 9999999)
    cursor = cxn.cursor()
    cursor.execute("SELECT * FROM pruebas.libro ORDER BY id DESC;")
    renglon = cursor.fetchone()
    if(renglon is not None):
        id = (int)(renglon[0])
    cxn.close()
    return id+1


def altaLibro():
    ok = True
    datosCompletos = False
    libro = Libro()
    dibujaPantallaCreate(libro)
    libro.setTitulo(input("título: "))
    dibujaPantallaCreate(libro)
    libro.setAutor(input("autor: "))
    dibujaPantallaCreate(libro)
    libro.setPaginas(input("página: "))
    dibujaPantallaCreate(libro)
    libro.setId(obtenSigId(getCxn()))
    dibujaPantallaCreate(libro)
    cxn = getCxn()
    try:
        cur = cxn.cursor()
        print(libro.toString())
        # INSERT INTO `pruebas`.`libro` (`id`, `titulo`, `autor`, `paginas`) VALUES (1, 'Título 1', 'Autor 1', '100');
        cur.execute("INSERT INTO pruebas.libro (id, titulo, autor, paginas) VALUES (%s,%s,%s,%s);",
                    (libro.getId(), libro.getTitulo(), libro.getAutor(), libro.getPaginas()))
        cxn.commit()
    except:
        ok = False
        print("----Unexpected error:", sys.exc_info())
        cxn.rollback()
    finally:
        cxn.close()
    return ok


def actualizaLibro():
    ok = True
    #
    consultaLibros()
    libro = Libro()
    idLibroABuscar = input("¿Qué libro [id] desea actualizar?")
    libro = obtenLibro(idLibroABuscar)
    print(libro.getTitulo())
    dibujaPantallaActualiza(libro)
    libro.setTitulo(input("título [{}] :".format(libro.getTitulo())))
    dibujaPantallaActualiza(libro)
    libro.setAutor(input("autor [{}] :".format(libro.getAutor())))
    dibujaPantallaActualiza(libro)
    libro.setPaginas(input("página [{}]: ".format(libro.getPaginas())))
    dibujaPantallaActualiza(libro)
    cxn = getCxn()
    try:
        cur = cxn.cursor()
        print(libro.toString())
        # UPDATE `pruebas`.`libro` SET `titulo` = 'Título 333', `autor` = 'Autor 33', `paginas` = '303' WHERE (`id` = '3');
        cur.execute("UPDATE pruebas.libro SET titulo=%s, autor=%s, paginas=%s WHERE id=%s;",
                    (libro.getTitulo(), libro.getAutor(), libro.getPaginas(), libro.getId()))
        cxn.commit()
    except:
        ok = False
        print("----Unexpected error:", sys.exc_info())
        cxn.rollback()
    finally:
        cxn.close()
    return ok


def borraLibro():
    ok = True
    consultaLibros()
    libro = Libro()
    idLibroABuscar = input("¿Qué libro [id] desea borrar?")
    libro = obtenLibro(idLibroABuscar)
    cxn = getCxn()
    try:
        cur = cxn.cursor()
        # DELETE FROM `pruebas`.`libro` WHERE (`id` = '4');
        cur.execute("DELETE FROM pruebas.libro WHERE id=%s;",
                    (libro.getId(),))
        cxn.commit()
    except:
        ok = False
        print("----Unexpected error:", sys.exc_info())
        cxn.rollback()
    finally:
        cxn.close()
    return ok


def consultaLibros():
    dibujaPantallaTrabajo(obtenLibros())


def leeAccionSiguiente():
    """Lee un caracter desde el teclado"""
    global accion
    global salir
    accion = (input("¿Qué operación desea realizar?: ")).upper()
    if accion == "X":
        salir = True
    elif accion == "C":
        altaLibro()
        consultaLibros()
    elif accion == "R":
        consultaLibros()
    elif accion == "U":
        actualizaLibro()
        consultaLibros()
    elif accion == "D":
        borraLibro()
        consultaLibros()
    else:
        print("operacion invalida")


# FLUJO PRINCIPAL
imprimeBienvenida()
consultaLibros()
while not salir:
    leeAccionSiguiente()
imprimeDespedida()
