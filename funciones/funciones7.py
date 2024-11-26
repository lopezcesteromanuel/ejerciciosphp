def aplicar_descuento(precio, descuento):
    return precio - (precio * (descuento / 100))

# Ejemplo de uso
precio_final = aplicar_descuento(100, 15)
print(precio_final)