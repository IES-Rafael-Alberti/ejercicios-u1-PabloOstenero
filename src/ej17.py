#
# Ej17: Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
# imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
#

nombre = input("Escribe tu nombre: ")
rep = int(input("Escribe el número de veces que quieres que se muestre por pantalla: "))

for i in range(0, rep):
    print(nombre)