#
# Ej03: Suponiendo que se han ejecutado las siguientes sentencias de asignación: 
#     ancho = 17
#     alto = 12.0
# Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:
#     1. ancho / 2
#     2. ancho // 2
#     3. alto / 3
#     4. 1 + 2 * 5
# Cuando termines comprueba con el intérprete si has acertado.
#

ancho = 17
alto = 12.0

print(f"ancho / 2 = {ancho / 2} y es de tipo {type(ancho/2)}")
print(f"ancho // 2 = {ancho // 2} y es de tipo {type(ancho//2)}")
print(f"alto / 3 = {alto / 3} y es de tipo {type(alto / 3)}")
print(f"1 + 2 * 5 = {1 + 2 * 5} y es de tipo {type(1 + 2 * 5)}")
print(f"ancho / alto = {ancho / alto} y es de tipo {type(ancho/alto)}")
print(f"ancho * 2 = {ancho * 2} y es de tipo {type(ancho*2)}")
print(f"ancho * alto = {ancho * alto} y es de tipo {type(ancho*alto)}")
print(f"(5 + 1 * 3) = {(5 + 1) * 3} y es de tipo {type((5 + 1) * 3)}")
print(f"(5 + 1 / 3) = {(5 + 1) / 3} y es de tipo {type((5 + 1) / 3)}")