#
# Ej23: Escribir un programa que pregunte el correo electrónico del usuario en la consola 
# y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
#

dominio = "@ceu.es"
correo = "nocorreo"

while correo.find("@") == -1:
    correo = input("Escribe tu dirección de correo electrónico: ")
    if correo.find("@") != -1:
        correo_nuevo = correo.split("@")[0] + dominio
    else:
        print("Lo que has escrito no es un correo electrónico")

print(correo_nuevo)