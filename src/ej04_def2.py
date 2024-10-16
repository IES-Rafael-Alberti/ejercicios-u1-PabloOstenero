#
# Ej04: Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
# la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
#

def calcular_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2) 

def main():

    fahrenheit = float(input("Escribe la temperatura en  grados Fahrenheit: "))
    
    celsius = calcular_celsius(fahrenheit)

    print("%.2f" % celsius + "ºC (" + "%.2f" % fahrenheit + "ºF)")

if __name__ == "__main__":
    main()