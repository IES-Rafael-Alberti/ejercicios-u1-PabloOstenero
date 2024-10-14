#
# Ej30: Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.
#

def serie(inicio, incremento, total):
    serie = "Serie => "
    i = inicio

    while i<total:
        if i == inicio or i+incremento >= total:
            serie = serie + str(i) + "-"
        else:
            serie = serie + str(i) + ".."
        
        i += incremento

    serie = serie + str(i)

    return serie

def main():
    inicio = -1
    total = -1
    
    while inicio < 1:
        inicio = int(input("Escribe un número de inicio para la serie: "))
        if inicio < 1:
            print("Tienes que escribir un número superior a 0.\n")

    incremento = int(input("Escribe un número para el incremento de la serie: "))

    while total < 1:
        total = int(input("Escribe el número total de la serie: "))
        if total < 1:
            print("Tienes que escribir un número superior a 0.\n")
    
    serie_final = serie(inicio, incremento, total)

    print(serie_final)

if __name__ == "__main__":
    main()