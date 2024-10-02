#
# Ej25: Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y 
# muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione 
# cuando el día o el mes se introduzcan con un solo carácter.
#

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
check = False

while check == False:
    fecha = input("Escribe la fecha de tu nacimiento en formato dd/mm/aaaa: ")
    
    if fecha.find("/") == -1:                                                         #Comprueba si el formato es correcto
        print("Tienes que usar el formato dd/mm/aaaa")
    else:
        dia = int(fecha.split("/")[0])
        mes = int(fecha.split("/")[1])
        año = int(fecha.split("/")[2])

        if dia<1 or dia >31:                                                           #Comprueba si el número de días no se pasa de lo normal
            print("Este número de días no tiene sentido")
        else:
            if mes<1 or mes>12:                                                        #Comprueba que el mes exista
                print("Este mes no existe")
            else:
                if ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia == 31)):  #Para los meses que tienen 30 días no deja poner el dia 31
                    print(f"{meses[mes-1]} no tiene 31 dias")
                elif mes == 1 and año%4 != 0 and dia >= 29:                            #Comprueba los días de febrero porque es especialito
                    print(f"{meses[mes-1]} no tiene {dia} días")
                elif mes == 1 and año%4 == 0 and dia >= 30:
                    print(f"{meses[mes-1]} no tiene {dia} días")
                else:                                                                  #Si todo es correcto entra aquí y hace que salga del bucle
                    check = True


print(f"Naciste el día {dia} de {meses[mes-1]} del {año}")