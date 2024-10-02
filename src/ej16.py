#
# Ej16: Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
# el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
#

pan_precio = 3.49
descuento = 0.6

pan_vend = int(input("Escribe el número de barras de pan que no son del día vendidas hoy: "))

print(f"El precio habitual de las barras de pan es {pan_precio}, por no ser fresca tiene un descuento del {int(descuento*100)}% y el coste de las barras de pan no frescas es {round(pan_vend * (pan_precio *(1-descuento)), 2)}")