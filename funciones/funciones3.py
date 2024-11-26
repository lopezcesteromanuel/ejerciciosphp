def convertir_temperatura(temperatura, escala):
    if escala == "C":
        return (temperatura * 9/5) + 32  # Celsius a Fahrenheit
    elif escala == "F":
        return (temperatura - 32) * 5/9  # Fahrenheit a Celsius
    else:
        return "Escala no válida"

# Ejemplo de uso
print(convertir_temperatura(25, "C"))
print(convertir_temperatura(77, "F"))