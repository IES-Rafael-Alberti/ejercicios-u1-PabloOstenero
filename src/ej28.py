#
# Ej28: Realiza un programa en Python que lea dos números enteros, 
# muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.
#

def main():

    num1 = 1
    num2 = num1

    while(num1 == num2):
        num1 = int(input("Escribe un número entero: "))
        num2 = int(input("Escribe otro número entero que no sea el mismo: "))

        if (num1 == num2):
            print("Los números no pueden ser iguales\n")

    if num1 < num2:
        print(f"El número menor es el {num1} y entre ellos existen {num2-num1} números enteros")
    else:
        print(f"El número menor es el {num2} y entre ellos existen {num1-num2} números enteros")

if __name__ == "__main__":
    main()