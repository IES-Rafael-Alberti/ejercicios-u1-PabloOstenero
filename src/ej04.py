#
# Ej04: Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#

celsius = float(input("Dime la temperatura en Celsius: "))

print(f"La temperatura en grados Fahrenheit es {round((celsius * 9/5) + 32, 2)}ºF ({round(celsius, 2)}ºC)")