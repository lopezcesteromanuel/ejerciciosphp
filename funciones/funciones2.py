def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    return imc, categoria

# Ejemplo de uso
imc, categoria = calcular_imc(70, 1.75)
print(imc, categoria)