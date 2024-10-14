#
# Ej08: Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.
#

cont = 0

print("Escribe tres números:")

num = float(input())
cont += num
num = float(input())
cont += num
num = float(input())
cont += num

print(f"La suma de los 3 números es {round(cont, 2)}")