#
# Ej27: Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
# muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
#

def precio_unitario(num, dig):
    num = round(num, 2)
    cadena = str(num)

    cadena = "0"*dig + cadena

    return cadena


def main():
    nombre = input("Escribe el nombre del producto: ")
    precio = float(input("Dime el precio del producto: "))
    unidades = int(input("Dame un número de unidades: "))

    coste_total = precio * unidades

    cadena = nombre + " " + precio_unitario(precio, 6) + " " + precio_unitario(coste_total, 8)

    print(cadena)

if __name__ == "__main__":
    main()