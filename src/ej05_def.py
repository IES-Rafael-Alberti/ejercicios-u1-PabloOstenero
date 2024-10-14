#
# Ej05: Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar 
# y calcule e imprima por pantalla el precio final del artículo.
#

def precio_final(precio, iva):
    print(f"El precio del producto con IVA es {round(precio * iva, 2)}")


def main():
    precio = float(input("Escribe el precio del producto sin IVA: "))
    iva = float(input("Dime el porcentaje de IVA: "))
    iva = (iva / 100) + 1

    precio_final(precio, iva)

if __name__ == "__main__":
    main()