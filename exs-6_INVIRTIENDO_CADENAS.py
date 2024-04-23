# /* #6_INVIRTIENDO_CADENAS
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

def invertString(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    print(inverted_string)

invertString('Hola mundo')