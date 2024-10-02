#
# ej01: Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
#

def saludo(nombre):
    return "Hola, " + nombre + "."

def main():
    nombre = input("Escribe tu nombre: ")

    print (saludo(nombre))

if __name__ == "__main__":
    main()