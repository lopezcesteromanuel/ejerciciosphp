def calcular_area_perimetro(largo, ancho):
    area = largo * ancho
    perimetro = 2 * (largo + ancho)
    return [area, perimetro]

# Ejemplo de uso
resultado = calcular_area_perimetro(5, 3)
print(resultado)