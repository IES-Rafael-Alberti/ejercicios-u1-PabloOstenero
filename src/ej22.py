#
# Ej22: Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y 
# después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
#

vocal = "b"
frase = input("Introduce una frase: ")

while vocal!="a" and vocal!="e" and vocal!="i" and vocal!="o" and vocal!="u":
    vocal = input("Introduce una vocal: ")
    if vocal!="a" and vocal!="e" and vocal!="i" and vocal!="o" and vocal!="u":
        print(f"Tienes que escribir una vocal, no {vocal}.")

print(frase + vocal.upper())