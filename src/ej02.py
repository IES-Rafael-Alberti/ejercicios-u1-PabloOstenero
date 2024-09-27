#
# Ej02: Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
#

horas_trabajo = int(input("Horas de trabajo: "))
coste_horas = int(input("Coste por horas: "))

print(f"Importe total: {horas_trabajo * coste_horas}")