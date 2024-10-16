#
# Ej11: Escribir un programa que lea un entero positivo, n, 
# introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma= n(n+1)/2
#

def factorial(n):
    suma = (n*(n+1))/2
    return f"La suma de todos los números desde 1 hasta {n} es: {suma}"

def main():
    n = -1
    while n<0:
        n = int(input("Escribe cualquier número entero: "))
        if n<0:
            print("El número debe ser mayor que 0")

    resutado = factorial(n)

    print(resutado)

if __name__ == "__main__":
    main()