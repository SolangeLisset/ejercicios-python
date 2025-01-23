from random import randint

print("*** Sistema de generador de ID unico ***")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido")
anio_nacimiento = (input("Ingrese su año de nacimiento yyyy"))

nombre = nombre.strip().upper()[0:2]
apellido = apellido.strip().upper()[0:2]
anio_nacimiento = anio_nacimiento.strip()[2:]

aleatorio = randint(1000,9999)
id_unico = f"{nombre}{apellido}{anio_nacimiento}{aleatorio}"
print(id_unico)