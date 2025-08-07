
from API import obtener_departamentos, obtener_obras


def main():
    departamentos = obtener_departamentos()
    obras = []
    print("Bienvenidos")

    while True:
        print("Que desea hacer?")
        print("1. Ver lista de obras por Departamento")
        print("2. Ver lista de obras por Nacionalidad del autor")
        print("3. Ver lista de obras por nombre del autor")
        print("3. Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print("Ver lista de obras por Departamento")
            ver_obras_por_departamento(departamentos, obras)
        elif opcion == "2":
            print("Ver lista de obras por Nacionalidad del autor")
            ver_obras_por_nacionalidad(obras)
        elif opcion == "3":
            print("Ver lista de obras por nombre del autor")
            ver_obras_por_nombre_autor(obras)
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Opcion no valida, intente de nuevo")

def ver_obras_por_departamento(departamentos, obras):
    for departamento in departamentos:
        print(f"ID: {departamento.id} - Departamento: {departamento.nombre}")

    id_departamento = input("Ingrese el ID del departamento: ") 
    while not id_departamento.isnumeric():
        print("ID invalido, intente de nuevo")
        id_departamento = input("Ingrese el ID del departamento: ")


    id_departamento = int(id_departamento)

    for obra in obras:
        if obra.tipo == id_departamento:
            pass

def ver_obras_por_nacionalidad(obras):
    nacionalidades = []

    for i, nacionalidad in enumerate(nacionalidades):
        print(f"{i+1}. {nacionalidad}.")

    seleccion = input("Ingrese el numero de la nacionalidad: ") 
    while not seleccion.isnumeric() or not int(seleccion) in range(1, len(nacionalidades)+1):
        print("numero invalido, intente de nuevo")
        seleccion = input("Ingrese el numero de la nacionalidad: ") 

def ver_obras_por_nombre_autor(obras):
    
    nombre = input("Ingrese el nombre del autor: ")
    while not nombre:
        print("Nombre invalido, intente de nuevo")
        nombre = input("Ingrese el nombre del autor: ")

    

    



main()