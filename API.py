import requests
import json
from Departamento import Departamento
from Obra import Obra
import csv

def obtener_nacionalidades(nacionalidades):

    with open("CH_Nationality_List_20171130_v1.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] != "Nationality":
                nacionalidades.append(row[0])

def obtener_departamentos():
    #Obtiene la lista de departamentos del Met Museum
    api_url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(api_url)

    #Si la respuesta es exitosa, devuelve la lista de departamentos con sus datos
    if response.status_code == 200:
        data = response.json()["departments"]

        #crea y guarda los objetos
        departamentos = []
        for departamento in data:
            departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))

        return departamentos

def obtener_obras_por_departamento(id_departamento, obras):
    #Obtiene las obras de un departamento por su ID
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={id_departamento}&q=*&hasImages=true"
    response = requests.get(api_url)

    #Si la respuesta es exitosa, devuelve el listado de id de obras
    if response.status_code == 200:
        data = response.json()["objectIDs"]
        if data is None:
            return []
        else:
            for id in data:

                #verifica si la obra ya existe en la lista
                existe = False
                for obra in obras:
                    if obra.id == id:
                        existe = True
                        break
                
                #si no existe, obtiene la obra por su id y la agrega a la lista
                if existe == False:
                    obra = obtener_obras_id(id)
                    if obra is not None:
                        obras.append(obra)

    return data

def obtener_obras():
    #Obtiene la lista de obras del Met Museum
    api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    response = requests.get(api_url)

    #Si la respuesta es exitosa, devuelve el listado de id de obras
    if response.status_code == 200:
        data = response.json()["objectIDs"]
        
        #crea y guarda los objetos
        obras = []
        for id in data:
            obra = obtener_obras_id(id)
            if obra is not None:
                obras.append(obra)

        return obras
    return []

def obtener_obras_id(id):
    #Obtiene los datos de una obra por su ID
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}"
    response = requests.get(api_url)
    
    #Si la respuesta es exitosa, devuelve el objeto obra
    if response.status_code == 200:
        obra_data = response.json()
        obra = Obra(obra_data["objectID"], obra_data["title"], obra_data["artistDisplayName"], obra_data["artistNationality"], obra_data["artistBeginDate"], obra_data["artistEndDate"], obra_data["department"], obra_data["objectDate"], obra_data["primaryImageSmall"])
        return obra
    return None

def obtener_obras_por_nacionalidad(nacionalidad, obras):
    #Obtiene las obras de un artista por su nacionalidad
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad.lower()}"
    response = requests.get(api_url)

    #si la respuesta es exitosa, devuelve el listado de id de obras
    if response.status_code == 200:
        data = response.json()["objectIDs"]
        #print(response.json())

        #crea y guarda los objetos
        for id in data:
            #print(id)

            #verifica si la obra ya existe en la lista
            existe = False
            for obra in obras:
                if obra.id == id:
                    existe = True
                    break
            
            #si no existe, obtiene la obra por su id y la agrega a la lista
            if existe == False:
                obra = obtener_obras_id(id)
                if obra is not None:
                    obras.append(obra)
        return data
    return []

def obtener_obras_por_artista(nombre, obras):

    nombre_sin_espacio = nombre.replace(" ", "%20")
    nombre_en_minusculas = nombre_sin_espacio.lower()

    #Obtiene las obras de un artista por su nombre
    api_url = "https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q=" + nombre_en_minusculas
    response = requests.get(api_url)

    #Si la respuesta es exitosa, devuelve el listado de id de obras
    if response.status_code == 200:
        data = response.json()["objectIDs"]
        

        #crea y guarda los objetos
        for id in data:

            #verifica si la obra ya existe en la lista
            existe = False
            for obra in obras:
                if obra.id == id:
                    existe = True
                    break
            
            #si no existe, obtiene la obra por su id y la agrega a la lista
            if existe == False:
                obra = obtener_obras_id(id)
                if obra is not None:
                    obras.append(obra)
        return data
    return []
            