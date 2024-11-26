import statistics

def calcular_promedio_mediana(numeros):
    promedio = sum(numeros) / len(numeros)
    mediana = statistics.median(numeros)
    return [promedio, mediana]

# Ejemplo de uso
resultado = calcular_promedio_mediana([1, 2, 3, 4, 5])
print(resultado)