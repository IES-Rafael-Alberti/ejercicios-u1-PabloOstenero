#
# Ej02: Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
#

def Importe(horas, coste):
    return horas * coste

def main():
    horas_trabajo = float(input("Horas de trabajo: "))
    coste_horas = float(input("Coste por horas: "))

    print(f"Importe total: {Importe(horas_trabajo, coste_horas)}€")

if __name__ == "__main__":
    main()