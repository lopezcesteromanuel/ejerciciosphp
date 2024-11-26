import re

def validar_contraseña(contraseña):
    if len(contraseña) > 8 and re.search(r'[A-Z]', contraseña) and re.search(r'[a-z]', contraseña) and re.search(r'\D', contraseña):
        return True
    return False

# Ejemplo de uso
print(validar_contraseña("Contraseña123"))
print(validar_contraseña("12345678"))