#
# Ej26: Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y 
# muestre por pantalla cada uno de los productos en una línea distinta.
#

i = 0

lista = input("Escribe la lista de la compra separados por comas. \n")

while i<len(lista.split(",")):
    print(lista.split(", ")[i])
    i += 1