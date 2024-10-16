#
# Ej05: Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar 
# y calcule e imprima por pantalla el precio final del artículo.
#

def precio_final(precio, iva):
    if iva < 0 or iva > 100:
        iva = 21
    
    return f"El precio final del artículo con IVA ({iva:.2f}) es {(precio * ((iva/100) + 1)):.2f}€."


def main():
    precio = float(input("Escribe el precio del producto sin IVA: "))
    iva = float(input("Dime el porcentaje de IVA: "))

    cadena = precio_final(precio, iva)

    print(cadena)

if __name__ == "__main__":
    main()