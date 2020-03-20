# [P14]
# python
import sys
print("hola mundo")
# [P15]
# sys.exit()
# [P16]
# HolaMundo.py
# [P19]
# $python
x = 1000
type(x)
# [P20]
# $python
2+2
1/2
1//2
# [P21]
# $python
0xAF
0o10
0b1011010010
# [P22]
# $python
x = 3
x*2
# [P24]
# $python
input("The meaning of life: ")
# The meaning of life: 42
# '42'
input("x:")
# x:hola
# 'hola'
input("y:")
# y:5
# '5'
# [P27]
# $python
2**3
pow(2, 3)
# [P29]


def fib(n):  # sucesión fibonacci
    a, b = 0, 1
    print("a:"+str(a))
    print("b:"+str(b))
    r = []  # r obtendrá el resultado
    while b < n:
        r.append(b)
        a, b = b, a+b
        # temp = a
        # a = b
        # b += temp
    return r


print(fib(10))
# [P32]
# $python


def sinArgumentos():
    print("No tengo Argumentos")


sinArgumentos()
# [P31]
# $python
a = 42  # Definición de una variable global


def someFunction():
    print("Variable global:  %d" % a)  # llamada de la variable global


someFunction()  # llamada de la función
# [P39]
# $python
x = 1
y = 1
bool(x == y)  # True

# [P42]
# $python
True  # True
False  # False
True == 1  # True
False == 0  # True
True + False + 42  # 43

# [P47]
# $python
x = 1
if(x == 1):
    print("1")

# [P48]
# $python
pwd = input('Ingrese la contraseña\n')
if pwd == 'Alfred':
    print('Bienvenido')
else:
    print('Acceso denegado...')

# [P49]
# $python
# sangrado
i = 5  # variable inicializada.

if i > 4:  # declaración de if.
    print("Línea Comando dentro del if")  # línea dentro de if
else:  # declaración else
    print("línea dentro del else")  # declaración print

print("Línea fuera del sangrado")  # línea fuera de la sangría

# [P57]
# $python
x = 1
while x <= 100:
    print(x)
    x += 1

# [P58]
# $python
#while 1 == 1:
i = 0
while i <= 3:
    name = input("Ingrese su nombre: ")
    print("Hola, {}!".format(name))
    i += 1

# [P59]
# $python
words = ['this', 'is', 'an', 'example']
for word in words:
    print(word)

# [P62]
# $python
"doesn't"  # "doesn't"
'"Si," le dijo.'  # '"Si," le dijo.'
"\"Si,\" le dijo."  # '"Si," le dijo.'
'"Isn\'t," she said.'  # '"Isn\'t," she said.'

# [P63]
# $python
'cad' 'ena'  # ‘cadena’
'prueba ' 'en ' 'python '  # 'prueba en python '

# [P65]
# $python
c = "una cadena"
c.upper()  # 'UNA CADENA'

c = "CADENA"
c.lower()  # 'cadena'

# [P70]
# $python
cadena = "cadena"
len(cadena)
max(cadena)
min(cadena)

# [P75]
# $python

lista = [7, 5, 3, 1, 0]
lista = [1, 2.3, "hola", 'fin']
lista

s = [1, 1+1, 6/2]
s

# [P76]
# $python

# Comentario
print("Hola Mundo")

# manejo de Listas
a = [1, 2, 3, 4, 5]  # Declaración de Lista de números
# Se imprimen las posiciones seleccionadas, notación [posinicial:posfinal-1]
print("Arreglo cortado %s " % str(a[2:4]))

a[2:4] = [3, 4, 5, 6]  # Añadimos más elementos a Lista
print("\nLista con elementos nuevos: %s" %
      str(a))  # se imprime de nuevo la lista

a[2:-1] = []  # en la posicion 2 y -1 cambiar por vacio
print("\nLista sin elementos vacios: %s" %
      str(a))  # se imprime de nuevo la lista

# [P78]
# $python

# insert(i, x)
# Inserta el elemento x en la posición i(después de la inserción, x ocupará la posición i)
lista = [1, 2, 3, 4, 5]
lista.insert(2, 8)
print(lista)  # [1, 2, 8, 3, 4, 5]
# append(x)
# Añade el elemento x al final de la lista
lista = [1, 2, 3, 4, 5]
lista.append(7)
print(lista)  # [1, 2, 3, 4, 5, 7]
# index(x)
# Devuelve el índice del primer elemento de la lista igual a x
lista = [1, 2, 3, 4, 5]
print(lista.index(2))  # 1
# remove(x)
# Elimina el primer elemento de la lista igual a x
lista = [1, 2, 3, 4, 5]
lista.remove(3)
print(lista)  # [1, 2, 4, 5]
# sort()
# Ordena los elementos de la lista
lista = [1, 5, 2, 4, 3]
lista.sort()
lista.sort(reverse=True)
lista = ["qaz", "asdf", "qwerty"]
lista.sort(key=len)
print(lista)
# reverse()
# Invierte el orden de los elementos de la lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
# count(x)
# Cuenta el número de veces que x aparece en la lista
lista = [1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 7]
lista.count(6)

# [P80]
# $python
# Tupla
a = (1, 2, 3)  # Se Añaden elementos a la Tupla.
print("Elementos de la Tupla: %s" % str(a))  # Se imprimen los elementos

# a[1] = 9  # Error

# [P81]
# $python
# Diccionarios (Vectores Asociativos)
tel = {}  # Se declara un Diccionario vacío.

tel["Luis"] = 5231428
#
tel["Maria"] = 3345625  # En estas 3 líneas se añaden elementos.
tel["Pepe"] = 2323888
#

print(tel)  # Se imprime el diccionario completo.

print(tel["Maria"])  # Se imprime un elemento en específico.

print("pepe" in tel)  # Pregunta si existe "pepe" en tel.

# [P84]
# Entrada y Salida
print(2+3, 4+5)  # imprime con espacio cada suma

# [P85]
# Entrada y Salida con formato
n = 4
m = 0.5
print("Resumen: %d datos, media %g. " % (n, m))

# [P86]
# Abriendo Archivo
#archivo = open("C:\\archivo.txt", "r")
archivo = open("slides/archivo.txt", "r")
contenido = archivo.read()
print("el contenido del archivo es:\n %s" % str(contenido))

# [P92]
#while True:
i = 0
while i < 3:
    print("Hola Mundo")
    i += 1

# [P93]
# $python
# 10 * (1/0)
# 4+spam*3
# '2'+2

# [P94]
#while True:
i = 0
while i < 3:
    i += 1
    try:
        x = int(input(u"Por favor ingrese un número: "))
        break

    except ValueError:
        print(u"OOps! no es un dato válido. Intente nuevamente")

# [P96]


class MiError(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return repr(self.valor)


try:
    raise MiError(2*2)
except MiError as e:
    print("Ocurrió mi excepción, valor: ", e.valor)

# [P97]
try:
    raise KeyboardInterrupt
except KeyboardInterrupt as kb:
    print("KeyboardInterrupt Lanzada")
finally:
    print("Chau, mundo")

# [P98]
with open("slides/archivo.txt") as f:
    for línea in f:
        print(línea)

f = open("slides/archivo.txt")
try:

    print(f.readlines())
    print("f.closed:"+str(f.closed))
except FileNotFoundError:
    print("Archivo no localizado")
finally:
    f.close()
    print("f.closed:"+str(f.closed))

# [P101]


class ClasePrueba:
    pass


# [P103]
objeto = ClasePrueba()
objeto.x = 45
objeto.y = 54

print("Atributo de 'objeto'", objeto.x)

# [P104]


class ClasePrueba:
    def hazAlgo(self):
        print("Realizando una acción")

# [P1050]


class Prueba:
    def __init__(self, var):
        self.var = var

# [P106]


# class ClaseDerivada(ClaseBase):
#    <declaración-1 >
#    .
#    .
#    .
#    <declaración-N >

# [P107]

# class ClaseDerivada(Base1, Base2, Base3):
#   <declaración-1>
#   .
#   .
#   .
#   <declaración-N>

# [P112]
#mysql_slides.py

