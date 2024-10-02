#
# Ej08: Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.
#

cont = 0

print("Escribe tres números:")

num = int(input())
cont += num
num = int(input())
cont += num
num = int(input())
cont += num

print(f"La suma de los 3 números es {cont}")