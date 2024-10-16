import random

def main():
    num_aleatorio = random.randint(1, 100)

    print("En este programa hay un número entero entre el 1 y el 100. Adivínalo: ")

    intento = int(input())

    if intento == num_aleatorio:
        print("Felicidades!!!! Has acertado a la primera")
    else:
        while intento != num_aleatorio:
            if intento < num_aleatorio:
                if intento <= num_aleatorio/2:
                    print("Uf estas muy lejos, es más alto")
                else:
                    print("Estas cerca!!, aunque es algo más alto")
            
            else:
                if intento <= num_aleatorio*2:
                    print("Estas cerca!!, aunque es algo más bajo")
                else:
                    print("Uf estás muy lejos, es más bajo")

            intento = int(input())

        print("Felicidades!!! Has acertado")

if __name__ == "__main__":
    main()