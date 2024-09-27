#
# Ej05: Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar 
# y calcule e imprima por pantalla el precio final del artículo.
#

precio = float(input("Escribe el precio del producto sin IVA: "))

iva = float(input("Dime el porcentaje de IVA: "))

iva = (iva / 100) + 1

print(f"El precio del producto con IVA es {precio * iva}")