# Ejemplo con Diccionario

print("\n=== DICCIONARIO ===")

# Crear el diccionario con información ficticia
información_personal = {
    "nombre": "José Cabrera",
    "edad": 30,
    "ciudad": "Cuenca",
    "profesión": "Ingeniero en Tecnología de la Información"
}
print("Diccionario original:", información_personal)

# Modificar la clave "ciudad"
información_personal["ciudad"] = "Guayaquil"
print("Datos actualizados 'ciudad':", información_personal)

# Agregar una nueva clave-valor "profesion"
información_personal["profesión"] = " Especialista en Cybeseguridad"
print("Datos actualizados 'profesión':", información_personal)

# Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in información_personal:
    información_personal["telefono"] = "0912345678"
print("Datos actualizados 'telefono':", información_personal)

# Eliminar la clave "edad"
del información_personal["edad"]
print("Datos actualizados 'edad':", información_personal)

# Diccionario resultante
print("Datos actualizados:", información_personal)
