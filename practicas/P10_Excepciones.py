# PRÁCTICA 9
# Crear un archivo de texto que contenga números y en alguna posición una cadena o letra
# Hacer un programa que lea todas las líneas del archivo y que muestre una excepción en caso de que lea algo diferente a  un número


try:
    f = open("P10_Excepciones.datos")
    datosSinProcesar = f.readlines()
    datosProcesados = []
    for dato in datosSinProcesar:
        try:
            datoNumero = int(dato)
        except ValueError as ve:
            print("Ex: " + str(ve))
        else:
            datosProcesados.append(dato)
except FileNotFoundError as fnfe:
    print("Ex: " + str(fnfe))

except:
    print("Excepción general")
else:
    print("Datos Procesados")
    print(datosProcesados)
finally:
    print("cerrando recursos")
    f.close()
