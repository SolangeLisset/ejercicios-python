#Generador de Emails

print("*** Generador de Email ***")

nombre = " Solange Castillo "

print(f"Nombre de usuario: {nombre}")

#normalizar el nombre
nombre_usuario = nombre.strip()


#reemplazar los espacios en blanco por puntos
nombre_usuario = nombre_usuario.replace(" ", ".")
nombre_usuario = nombre_usuario.lower()
print(f"Nombre de usuario Normalizado: {nombre_usuario}")

empresa = " Inacap "
print(f"Nombre de empresa {empresa}")
extension_dominio = ".com "
print(f"Extension del dominio: {extension_dominio}")

#quitamos los espacios en blanco
nombre_empresa_normalizado = empresa.replace(" ","").lower()
dominio_email = f"@{nombre_empresa_normalizado}{extension_dominio}"
print(f"Dominio del email normazalido: {dominio_email}")

#Se imprime el email generado
email_final = nombre_usuario + dominio_email
print(email_final)
print(f"\nEmail final generado: {email_final}")

