#
# Ej15: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.
#

interes = 0.04
año = ["primer", "segundo", "tercer"]
i = 0

capital = float(input("Escribe la cantidad de dinero que desea depositar: "))

while (i<3):
    capital = round(capital * (1+interes), 2)
    print(f"La cantidad de ahorros tras el {año[i]} año es {capital}")
    i += 1
