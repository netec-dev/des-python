
print("BIENVENIDO")
salir=False
while(not salir):
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
    salirStr = input("Desea salir de la aplicación [S]i/[N]o : ")
    if salirStr=="S":
        salir = True
    elif salirStr=="N":
        salir = False
    else:
        salir = False
    print("----------------------")
print("HASTA LA VISTA")