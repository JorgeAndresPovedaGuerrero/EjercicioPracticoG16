# este archivo contiene las funciones para procesar texto
"""
funcion para contar los caracteres de una cadena
parametros: la cadena a procesar
retorno: el numero de caracteres de la cadena de entrada
"""

# CONTAR CARACTERES


def contar_caracteres(cadena):
    cuenta = 0
    for i in range(len(cadena)):
        cuenta += 1
    return cuenta

def contar_a(cadena):
    contador = 0
    for i in cadena:
        if i == "a":
            contador += 1
    return contador

def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

