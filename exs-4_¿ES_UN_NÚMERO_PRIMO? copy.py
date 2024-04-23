# /* #4_¿ES_UN_NÚMERO_PRIMO?
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def isPrimo(j):
    while 1 < j:
        if i % j == 0:
            return False
        j -= 1
    return True

for i in range(2, 101):
    j = i - 1
    if isPrimo(j):
        print(i)