import os
import django
import requests
from .models import Perfil, Productos, Cliente

def obtener_y_guardar_datos_perfil():
    url = "http://18.221.57.79:8000/api/Perfil" 
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  

        for item in data:
            Perfil.objects.update_or_create(
                nombre_perfil=item["nombre_perfil"]  
            )

        print("Datos guardados exitosamente.")
    else:
        print("Error al obtener los datos:", response.status_code)
        
        
        
def obtener_y_guardar_datos_productos():
    url1 = "http://3.19.235.79:8000/api/productos/" 
    response1 = requests.get(url1)
    if response1.status_code == 200:
        data = response1.json()  

        for item in data:
            Productos.objects.update_or_create(
                descripcion=item["descripcion"],
                stock=item["stock"],
                ubicacion=item["ubicacion"]
                
            )

        print("Datos guardados exitosamente.")
    else:
        print("Error al obtener los datos:", response1.status_code)
        
        
def obtener_y_guardar_datos_clientes():
    url1 = "http://18.190.176.232:8000/api/clientes/" 
    response1 = requests.get(url1)
    if response1.status_code == 200:
        data = response1.json()  

        for item in data:
            Cliente.objects.update_or_create(
                nombre=item["nombre"],
                email=item["email"],         
            )

        print("Datos guardados exitosamente.")
    else:
        print("Error al obtener los datos:", response1.status_code)
