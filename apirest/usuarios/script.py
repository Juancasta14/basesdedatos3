import os
import django
import requests
from .models import Perfil, Productos, Cliente

def obtener_y_guardar_datos_perfil():
    urls = "http://18.221.57.79:8000/api/Perfil/"  
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = Perfil.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                Perfil.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    nombre_perfil =item["nombre_perfil"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")
        
        
        
def obtener_y_guardar_datos_productos():
    urls = "http://3.19.235.79:8000/api/productos/"  # API de cristian
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = Productos.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                Productos.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    descripcion =item["descripcion"],
                    stock =item["stock"],
                    ubicacion =item["ubicacion"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")
        
        
def obtener_y_guardar_datos_clientes():
    urls = "http://18.190.176.232:8000/api/clientes/"  
    response = requests.get(urls)

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = Cliente.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                Cliente.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    nombre =item["nombre"],
                    email =item["email"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")
