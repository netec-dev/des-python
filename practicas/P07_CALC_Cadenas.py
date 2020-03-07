import os
import time

ANCHO = 60
PAUSA = 2
operacion = "?"
numero1, numero2, resultado = 0.0, 0.0, 0.0
salir = False
LINEA_INICIAL = "|" + (":" * ANCHO) + "|"
LINEA_FINAL = "|" + (":" * ANCHO) + "|"
LINEA_VACIA = "|" + (" " * ANCHO) + "|"
LINEA_SEPARADOR ="|" + ("-" * ANCHO) + "|" 
LINEA_PLANTILLA = "|" + \
    ("[número 1] [operación] [número 2] = resultado".center(ANCHO)) + "|"


def imprimeBienvenida():
    """Imprime el mensaje de bienvenida del sistema"""
    dibujaPantallaPrincipal("B I E N V E N I D O  A  'MyCALC'")
    time.sleep(PAUSA)


def imprimeDespedida():
    """Imprime el mensaje de despedida del sistema"""
    dibujaPantallaPrincipal("H A S T A  P R O N T O")
    time.sleep(PAUSA)
    limpiaPantalla()


def dibujaPantallaPrincipal(mensaje):
    """Dibuja la pantalla principal (Inicial/Final)"""
    limpiaPantalla()
    print(LINEA_INICIAL)
    print(LINEA_VACIA)
    print("|" + (mensaje.center(ANCHO)) + "|")
    print(LINEA_VACIA)
    print(LINEA_FINAL)


def dibujaPantalla(mensaje=None):
    """Dibuja la pantalla de trabajo"""
    limpiaPantalla()
    print(LINEA_INICIAL)
    print(LINEA_PLANTILLA)
    print(LINEA_SEPARADOR)
    print("|" + (str(numero1) + " " + operacion +
                 " " + str(numero2) + " = " + str(resultado)).center(ANCHO) + "|")
    print(LINEA_FINAL)
    if(mensaje!=None):
        res = input(mensaje)
        return res
    else:
        return ""


def imprimeCaratula():
    """Imprime la pantalla principal del sistema"""
    dibujaPantalla()
    time.sleep(2)


def calculaResultado():
    """Calcula el resultado de la operación deseada"""
    global resultado
    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        resultado = numero1 / numero2
    return resultado


def leeNumero1():
    """Lee un número desde el teclado"""
    global numero1
    numero1Str = dibujaPantalla("[número 1] +̶,̶ ̶-̶,̶ ̶*̶,̶ ̶/̶  | n̶ú̶m̶e̶r̶o̶ ̶2̶  : ")
    if (numero1Str.isnumeric):
        numero1 = float(numero1Str)


def leeOperacion():
    """Lee un caracter desde el teclado"""
    global operacion
    opStr = dibujaPantalla("n̶ú̶m̶e̶r̶o̶ ̶1̶  [+ , - , * ó /] n̶ú̶m̶e̶r̶o̶ ̶2̶  : ")
    if (opStr.isalpha):
        operacion = opStr


def leeNumero2():
    """Lee un número desde el teclado"""
    global numero2
    numero2Str = dibujaPantalla("n̶ú̶m̶e̶r̶o̶ ̶1̶  | +̶,̶ ̶-̶,̶ ̶*̶,̶ ̶/̶  [número 2]: ")
    if (numero2Str.isnumeric):
        numero2 = float(numero2Str)


def limpiaPantalla():
    """Limpia la pantalla"""
    os.system('cls')


def continuar():
    """Determina si se termina o no la ejecución"""
    global salir
    continuarStr = input("| realizar otra operación: [s/n] ")
    if continuarStr == 's':
        salir = False
    else:
        salir = True


def reinicializarValores():
    """Reinicializa las variable globales"""
    global numero1, numero2, resultado, operacion
    numero1, numero2, resultado = 0.0, 0.0, 0.0
    operacion = '?'


# FLUJO PRINCIPAL
imprimeBienvenida()
while not salir:
    reinicializarValores()
    imprimeCaratula()
    leeNumero1()
    leeOperacion()
    leeNumero2()
    calculaResultado()
    imprimeCaratula()
    continuar()
imprimeDespedida()
