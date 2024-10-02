#
# Ej04: Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#

celsius = float(input("Dime la temperatura en Celsius: "))

print(f"La temperatura en Fahrenheit es {(celsius * 9/5) + 32}")