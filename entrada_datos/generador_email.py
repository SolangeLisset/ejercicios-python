#Generador de email


print("*** Generador de Email ***")
nombre = input("Ingrese su nombre: ")
#se convierte en minuscola y se le quita los espacios
nombre = nombre.lower().strip()
#se reemplaza el espacio en blanco por un punto
nombre = nombre.replace(" ", ".")
print(nombre)

apellido = input("Ingrese su apeliido")
#se le quita los espacios
apellido = apellido.lower().strip("")
#Se reemplaza los espacios por un punto
apellido = apellido.replace(" ", ".")
print(apellido)

nombre_empresa = input("Ingrese el nombre de la empresa")
#Se reemplaza los espacio por cadena vacia
nombre_empresa = nombre_empresa.replace(" ", "").lower()
domonio = input("Ingrese el nombre del dominio")

print(f"{nombre}{apellido}@{nombre_empresa}{domonio}")