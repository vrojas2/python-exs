# /* #3 LA SUCESIÓN DE FIBONACCI
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */

next = [0,1]
for i in range(0, 51):
    ancho = len(next)
    num2 = next[ancho-2]
    num1 = next[ancho-1]
    next.append(num2+num1)
print(next)
