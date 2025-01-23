#Sistema de empleados
print("*** Sistema de empleados ***")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
salario_empleado = float(input("Ingrese su salario: "))
jefe_departamento = input("Es jefe de departamento ?(SI o NO)")

jefe_departamento = jefe_departamento.lower() == "si"


print("\nDatos del empleado")
print(f"Nombre del empleado: {nombre}")
print(f"Edad del empleado: {edad}")
print(f"Salario del empleado: {salario_empleado:.2f}")
print(f"Es jefe del departamento: {jefe_departamento}")