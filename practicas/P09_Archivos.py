# PRÁCTICA 5
# En un archivo de texto escribir la entrada de la consola de un usuario y permitir que cada vez que se ejecute, el nuevo contenido sea agregado al archivo

SALTO_DE_LINEA = "\n"

archivo = open('P09_Archivos.dat', 'a')

cadenaEscritaPorElUsuario = input("Información a adicionar al archivo: \n")

archivo.write(cadenaEscritaPorElUsuario)
archivo.write(SALTO_DE_LINEA)

archivo.close()
