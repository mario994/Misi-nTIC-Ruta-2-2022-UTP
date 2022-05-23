print("--Aplicación CRUD Tareas Pendientes--")
print("")
print("1. Adicionar Tarea")
print("2. Consultar Tarea")
print("3. Actualizar Tarea")
print("4. Eliminar Tarea")
print("5. Salir")
print("")
opcion = int(input("Ingrese una opción: "))

tareas = {
    "01":{
        "descripcion": "Aprender Python",
        "estado": "En proceso",
        "tiempo": 60
    },
    "02": {
        "descripcion": "Aprender Ingles",
        "estado": "En proceso",
        "tiempo": 60
    },
    "03": {
        "descripcion": "Aprender Java",
        "estado": "No iniciado",
        "tiempo": 60
    }
}

def read():
    print("")
    print("-> Listado de Tareas")
    print("")

    for id, tarea in tareas.items():
        print(f"Identificador de la tarea  # {id}")
        for descripcion, atributo in tarea.items():
            print(f"{descripcion} : {atributo}")
        print("------------------")

#Create
if opcion == 1:
    print("")
    print("->Adicionando Tarea")
    print("")

    identificador = input("Ingrese un número identificador de la tarea: ")

    tareaNueva = {
        "descripcion": input("Ingrese la descripción de la Tarea: "),
        "estado": input("Ingrese el estado de la tarea: "),
        "tiempo": int(input("Ingrese el tiempo estipulado para la tarea: "))
    }

    tareas.update({identificador:tareaNueva})
    print("")
    print("Nueva tarea agregada exitosamente")
    print(tareas)

#Read

elif opcion == 2:
    read()

#Update
elif opcion == 3:
    read()
    idTarea = input("Ingresa el Id de la tarea que deseas actualizar ")
    tareas[idTarea] = {
        "descripcion": input("Ingrese la descripción de la Tarea: "),
        "estado": input("Ingrese el estado de la tarea: "),
        "tiempo": int(input("Ingrese el tiempo estipulado para la tarea: "))
    }
    print("")
    print("-> Listado de Tareas Actulizado Correctamente")
    read()

#Delete
elif opcion == 4:
    print("")
    read()
    tareas.pop(input("Ingresa el id de la tarea que deseas eliminar: "))
    print("Tarea Eliminada Correctamente")
    print("Esté es el nuevo listado de tareas")
    print("")
    read()
