#
# Ej06: Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado 
# y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%). 
#

precio = float(input("Escribe el precio final del producto: "))

print(f"El precio sin IVA del producto es {round(precio / 1.1, 2)}")