# /* #5_ÁREA_DE_UN_POLÍGONO
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def calcular_area_poligono(poligono):
    tipo = poligono["tipo"].lower()
    if tipo == "triangulo":
        base = poligono["base"]
        altura = poligono["altura"]
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
    elif tipo == "cuadrado":
        lado = poligono["lado"]
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")
    elif tipo == "rectangulo":
        base = poligono["base"]
        altura = poligono["altura"]
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    else:
        print("Polígono no soportado")

triangulo = {"tipo": "Triangulo", "base": 4, "altura": 5}
cuadrado = {"tipo": "Cuadrado", "lado": 3}
rectangulo = {"tipo": "Rectangulo", "base": 6, "altura": 8}

calcular_area_poligono(triangulo)
calcular_area_poligono(cuadrado)
calcular_area_poligono(rectangulo)
