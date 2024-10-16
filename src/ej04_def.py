#
# Ej04: Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#

def calcular_celsius():
    fahrenheit = float(input("Escribe la temperatura en  grados Fahrenheit: "))

    return "%.2f" % ((fahrenheit - 32) * 5/9) + "ºC (" + "%.2f" % fahrenheit + "ºF)"

def main():

    cadena = calcular_celsius()

    print(cadena)

if __name__ == "__main__":
    main()