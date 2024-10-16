#
# Ej24: Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y 
# muestre por pantalla el número de euros y el número de céntimos del precio introducido.
#

precio = round(float(input("¿Cuál es el precio del producto? \n")), 2)

print(f"Son {int(precio/1)}€ y {int(round(precio%1, 2) * 100)} céntimos.")