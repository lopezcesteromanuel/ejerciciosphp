def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Calcular primos entre 1 y un millón
primos = [i for i in range(1, 1000001) if es_primo(i)]
print(primos[:10])  # Mostrar los primeros 10 primos