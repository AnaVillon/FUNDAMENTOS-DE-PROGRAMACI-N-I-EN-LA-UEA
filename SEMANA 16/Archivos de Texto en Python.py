# Crear y escribir en el archivo my_notes.txt
with open("my_notes.txt", "w") as file:
    file.write("Hoy comencé a organizar mis tareas pendientes.\n")
    file.write("Necesito terminar el informe del proyecto para el viernes.\n")
    file.write("Recordar tomar un descanso y salir a caminar por la tarde.\n")

# Abrir el archivo my_notes.txt en modo lectura
file = open("my_notes.txt", "r")

# Leer línea por línea y mostrar en consola
linea = file.readline()
while linea:
    print(linea.strip())
    linea = file.readline()

# Cerrar el archivo después de leerlo
file.close()

# Resultado al correr
C:\Users\anavi\AppData\Local\Programs\Python\Python313\python.exe "C:\Users\anavi\PROGRAMACION\SEMANA 16\Archivos de Texto en Python.py"
Hoy comencé a organizar mis tareas pendientes.
Necesito terminar el informe del proyecto para el viernes.
Recordar tomar un descanso y salir a caminar por la tarde.

Process finished with exit code 0