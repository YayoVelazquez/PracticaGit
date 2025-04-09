def agregar_tarea():
    with open("tareas.txt", "a") as archivo:
        tarea = input("Escribe una nueva tarea: ")
        archivo.write(tarea + "\n")
        print("Tarea guardada.")

def ver_tareas():
    print("\nTus tareas:")
    with open("tareas.txt", "r") as archivo:
        print(archivo.read())

while True:
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        break
    else:
        print("Opción no válida")



