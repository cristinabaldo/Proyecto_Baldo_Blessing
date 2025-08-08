
from API import obtener_departamentos, obtener_obras, obtener_obras_por_artista, obtener_obras_por_departamento, obtener_nacionalidades, obtener_obras_por_nacionalidad
import requests
from PIL import Image

def main():
    departamentos = obtener_departamentos()
    obras = []
    nacionalidades = []
    obtener_nacionalidades(nacionalidades)
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
            ver_obras_por_nacionalidad(nacionalidades, obras)
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

    var = obtener_obras_por_departamento(id_departamento, obras)
    print(f"Buscando obras...")
    
    if var == []:
        print("No sexisten obras para este departamento o el ID es incorrecto")
    else:

        contador = 1
        for obra in obras:
            for id in var:
                if obra.id == id:
                    print(f"{contador}.")
                    obra.show()
                    contador += 1

        respuesta = input("Desea ver la imagen de alguna obra? 1. Si, 2. No: ")
        while respuesta not in ["1", "2"]:
            print("Opcion invalida, intente de nuevo")
            respuesta = input("Desea ver la imagen de alguna obra? 1. Si, 2. No: ")
        
        

        if respuesta == "1":
            respuesta = input("Ingrese el numero de la obra: ")
            while not respuesta.isnumeric() or not int(respuesta) in range(1, contador+1):
                print("Numero invalido, intente de nuevo")
                respuesta = input("Ingrese el numero de la obra: ")

            contador = 1
            for obra in obras:
                for id in var:
                    if obra.id == id:
                        if contador == int(respuesta):
                            mostrar_imagen(obra)
                            return
                        contador += 1

def ver_obras_por_nacionalidad(nacionalidades, obras):

    for i, nacionalidad in enumerate(nacionalidades):
        print(f"{i+1}. {nacionalidad}.")

    seleccion = input("Ingrese el numero de la nacionalidad: ") 
    while not seleccion.isnumeric() or not int(seleccion) in range(1, len(nacionalidades)+1):
        print("numero invalido, intente de nuevo")
        seleccion = input("Ingrese el numero de la nacionalidad: ")

    nacionalidad = nacionalidades[int(seleccion)-1]
    print(f"Buscando obras de nacionalidad {nacionalidad}...")
    data = obtener_obras_por_nacionalidad(nacionalidad, obras)

    if data == []:
        print("No sexisten obras con artistas de esta nacionalidad")
    else:

        contador = 1
        for obra in obras:
            for id in data:
                if obra.id == id:
                    print(f"{contador}.")
                    obra.show()
                    contador += 1

        respuesta = input("Desea ver la imagen de alguna obra? 1. Si, 2. No: ")
        while respuesta not in ["1", "2"]:
            print("Opcion invalida, intente de nuevo")
            respuesta = input("Desea ver la imagen de alguna obra? 1. Si, 2. No: ")
        
        

        if respuesta == "1":
            respuesta = input("Ingrese el numero de la obra: ")
            while not respuesta.isnumeric() or not int(respuesta) in range(1, contador+1):
                print("Numero invalido, intente de nuevo")
                respuesta = input("Ingrese el numero de la obra: ")
                
            contador = 1
            for obra in obras:
                for id in data:
                    if obra.id == id:
                        if contador == int(respuesta):
                            mostrar_imagen(obra)
                            return
                        contador += 1

def ver_obras_por_nombre_autor(obras):
    
    nombre = input("Ingrese el nombre del autor: ")
    while not nombre:
        print("Nombre invalido, intente de nuevo")
        nombre = input("Ingrese el nombre del autor: ")

    print(f"Buscando obras de {nombre}...")

    data = obtener_obras_por_artista(nombre, obras)
 
    if data == []:
        print("No sexisten obras para este departamento o el ID es incorrecto")
    else:

        contador = 1
        for obra in obras:
            for id in data:
                if obra.id == id:
                    print(f"{contador}.")
                    obra.show()
                    contador += 1

        respuesta = input("Desea ver la imagen de alguna obra? 1. Si, 2. No: ")
        while respuesta not in ["1", "2"]:
            print("Opcion invalida, intente de nuevo")
            respuesta = input("Desea ver la imagen de alguna obra? 1. Si, 2. No: ")
        
        

        if respuesta == "1":
            respuesta = input("Ingrese el numero de la obra: ")
            while not respuesta.isnumeric() or not int(respuesta) in range(1, contador+1):
                print("Numero invalido, intente de nuevo")
                respuesta = input("Ingrese el numero de la obra: ")
                
            contador = 1
            for obra in obras:
                for id in data:
                    if obra.id == id:
                        if contador == int(respuesta):
                            mostrar_imagen(obra)
                            return
                        contador += 1

def mostrar_imagen(obra):

    # URL de la API
    api_url = obra.imagen_url

    if api_url is None or api_url == "":
        print("No hay imagen disponible para esta obra.")
        
    else:
        # Nombre deseado para el archivo (sin extensión, ya que se determinará automáticamente)
        nombre_archivo_destino = obra.id
        
        # Llamar a la función para guardar la imagen
        nombre_archivo_destino=guardar_imagen_desde_url(api_url,nombre_archivo_destino)
        img = Image.open(nombre_archivo_destino)
        img.show()

def guardar_imagen_desde_url(url, nombre_archivo):
    """
    Descarga una imagen desde una URL y la guarda en un archivo.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Lanza excepción si hay error HTTP (4xx o 5xx)

        content_type = response.headers.get('Content-Type')
        extension = '.png'  # Valor por defecto

        if content_type:
            if 'image/png' in content_type:
                extension = '.png'
            elif 'image/jpeg' in content_type:
                extension = '.jpg'
            elif 'image/svg+xml' in content_type:
                extension = '.svg'

        nombre_archivo_final = f"{nombre_archivo}{extension}"

        with open(nombre_archivo_final, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")
        return nombre_archivo_final

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer el request: {e}")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

main()