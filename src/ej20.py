#
# Ej20: Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato y 
# muestre por pantalla el número de teléfono sin el prefijo y la extensión.
#

telefono = input("Escribe el número de teléfono de la empresa con el formato prefijo-número-extension (por ejemplo +34-913724710-56): ")

print(f"El número de teléfono sin prefijo o extensión es: {telefono.split("-")[1]}")