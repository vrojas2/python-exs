# /* #2 ¿ES UN ANAGRAMA?
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un qu consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

# palabra1 = input()
# palabra2 = input()

def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    palabra1_ordenada = sorted(palabra1)
    palabra2_ordenada = sorted(palabra2)
    
    if palabra1_ordenada == palabra2_ordenada:
        return True
    else:
        return False

# Ejemplo
palabra1 = "amor"
palabra2 = "roma"
es_anagrama = son_anagramas(palabra1, palabra2)
print(f"¿{palabra1} y {palabra2} son anagramas? {es_anagrama}")
