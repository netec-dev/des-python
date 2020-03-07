for x in range(4):
    print("\\")



# suma
a, b = "letra a", "letra b"
# ¿Cuál es la salida de ejecutar 'a+b'?
a + b
# multiplicación
c = "letra c"
c * 3

# comentarios en linea
""" comentarios
    multilínea"""

def hola(arg):
    """ El docstring de la función"""
    print("hola",arg, "!")

hola("plone")

help(hola)

print(hola.__doc__)

# Ejercicios con al menos tres funciones de cadenas
# Visitar https://docs.python.org/3.8/library/stdtypes.html#string-methods

print('%(language)s has %(number)03d quote types.' %  {'language': "Python", "number": 2})

