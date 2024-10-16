#
# Ej13: Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
# "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, 
# y c y r son el cociente y el resto de la división entera respectivamente.
#

print("Dame dos números para dividirlos: ")

dividendo = int(input())
divisor = int(input())

print(f"La división de {dividendo} entre {divisor} da un cociente {int(dividendo/divisor)} y un resto {dividendo%divisor}")