# Asignar a una variable la cadena “esto es un ejemplo”, y hacer que escriba en la pantalla “un ejemplo es esto” utilizando la notación de slices 
# Sugerencia: Haga un Split de la cadena y cree una nueva cadena con el nuevo orden

cadena = "esto es un ejemplo"
parteIzquierda = cadena[8:18]
parteCentral = cadena[5:7]
parteDerecha = cadena[0:4]

print(parteIzquierda)
print(parteCentral)
print(parteDerecha)

cadenaResultante = parteIzquierda + " " + parteCentral + " " + parteDerecha
print(cadenaResultante)

# split
cadenaSpliteada = cadena.split()
print(cadenaSpliteada)
cadenaResultante2 = cadenaSpliteada[2] + " " + cadenaSpliteada[3] + " " + cadenaSpliteada[1] + " " + cadenaSpliteada[0]
print(cadenaResultante2)