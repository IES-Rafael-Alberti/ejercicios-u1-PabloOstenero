#
# Ej29: Realiza un programa en Python que solicite un nombre y una edad.
#

def main():
    nombre = input("Escribe tu nombre: ")
    edad = -1
    
    while edad < 0 or edad > 125:
        edad = int(input("Escribe tu edad: "))

        if edad < 0 or edad > 125:
            print("La edad tiene que estar comprendida entre 0 y 125.\n")

    if nombre == "":
        nombre = "Desconocido"
    
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125-edad} años por cumplir")

if __name__ == "__main__":
    main()