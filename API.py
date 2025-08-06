import requests
import json
from Departamento import Departamento



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