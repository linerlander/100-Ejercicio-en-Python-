"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def invertir_palabra(palabra):
    for i in range(len(palabra) -1,-1,-1):
        print(palabra[i],end = ' ')
invertir_palabra('Hola mundo')