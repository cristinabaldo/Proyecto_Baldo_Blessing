


def main():
    
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
        elif opcion == "2":
            print("Ver lista de obras por Nacionalidad del autor")
        elif opcion == "3":
            print("Ver lista de obras por nombre del autor")
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Opcion no valida, intente de nuevo")