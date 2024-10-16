#
# Ej14: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que 
# deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos 
# y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
#

peso_payaso = 112
peso_muñeca = 75

num_payaso = int(input("Escribe el número de payasos que se han vendido en el último pedido: "))
num_muñeca = int(input("Escribe el número de muñecas que se han vendido en el último pedido: "))

print(f"El peso total del último pedido es {peso_payaso*num_payaso + peso_muñeca*num_muñeca}g.")