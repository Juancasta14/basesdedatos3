import os
import django
import requests
from .models import *
import csv

def sync_data(model, url, mapping):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            obj, created = model.objects.update_or_create(
                id=item["id"], defaults={key: item[value] for key, value in mapping.items()}
            )
            
            if created:
                print(f"Nuevo registro creado para ID {item['id']}")
            else:
                print(f"Registro con ID {item['id']} actualizado.")
        
        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")




def obtener_y_guardar_datos_perfil():  
    sync_data(Perfil, "http://18.221.57.79:8000/api/Perfil/", {
        "nombre_perfil": "nombre_perfil"
    })

def obtener_y_guardar_datos_clientes():
    sync_data(Cliente, "http://18.190.176.232:8000/api/clientes/", {
        "nombre": "nombre",
        "email": "email"
    })
        
        
        
def obtener_y_guardar_datos_productos():
    sync_data(Productos, "http://3.19.235.79:8000/api/productos/", {
        "descripcion": "descripcion",
        "stock": "stock",
        "ubicacion": "ubicacion"
    })
        
def importar_csv(ruta_csv):
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            DatosPrivados.objects.create(
                product_name=fila['product_name'],

            )


importar_csv('apirest/amazon.csv')       

