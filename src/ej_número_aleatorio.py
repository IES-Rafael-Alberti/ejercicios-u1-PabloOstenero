#
# Cálculo de un número aleatorio entre dos valores
#
import random

def dame_un_numero_aleatorio(min, max):
    return random.randint(min, max)

def main():
    print("Escribe dos valores entre los que tenga que salir el número aleatorio: ")
    
    min = int(input("Dime el mínimo: "))
    max = int(input("Dame el máximo: "))

    num_random = dame_un_numero_aleatorio(min, max)

    print(num_random)


if __name__ == "__main__":
    main()