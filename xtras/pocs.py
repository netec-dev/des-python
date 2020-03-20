print("Lanzando Excepciones")

try:
    print("Dentro del try - ANTES")
    variableDeclaradaEnTry = ":)"
    raise NameError("Soy una excepción")
    print("Dentro del try - DESPUÉS")
except NameError as ne:
    print("En except")
    print(variableDeclaradaEnTry)
    print(">>> " + ne.__str__())
    raise
    print("En except después de 'raise'")
else:
    print("En else")
    print(variableDeclaradaEnTry)
finally:
    print("En finally")
    print(variableDeclaradaEnTry)
