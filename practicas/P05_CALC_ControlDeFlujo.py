op1 = float(input("Ingrese el primer operando: "))
op2 = float(input("Ingrese el segundo operando: "))
print("[S]uma | [R]esta | [M]ultiplicación | [D]ivisión")
operacionAritmetica = input("Seleccione la operación aritmética a realizar: ")
if(operacionAritmetica == "S"):
    suma = op1+op2
    print("suma: " + str(suma))
elif(operacionAritmetica == "R"):
    resta = op1-op2
    print("resta: " + str(resta))
elif(operacionAritmetica == "M"):
    multiplicacion = op1*op2
    print("multiplicación: " + str(multiplicacion))
elif(operacionAritmetica == "D"):
    division = op1/op2
    print("división: " + str(division))
else:
    print("Opción no válida")
print("----------------------")