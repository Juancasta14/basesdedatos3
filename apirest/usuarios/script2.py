import os
import django
import csv
from datetime import datetime
from django.utils import timezone
from django.db import transaction, connection

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usuarios.settings')
django.setup()

from usuarios.models import Trip, Envio

FILE_PATH = os.path.expanduser("~/Escritorio/repo/basesdedatos3/apirest/apirest/DatosPrivadosCorreo.csv")

def convertir_fecha(fecha_str):
    """Convierte una cadena de fecha en objeto datetime, asegurando compatibilidad con zona horaria."""
    if not fecha_str or fecha_str.upper() == "NULL":
        return None  # Ahora sí deja los valores nulos

    if "." in fecha_str:
        fecha_str = fecha_str.split(".")[0]

    formatos = ["%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%Y/%m/%d", "%Y-%m-%d"]

    for formato in formatos:
        try:
            fecha = datetime.strptime(fecha_str, formato)
            return timezone.make_aware(fecha)
        except ValueError:
            continue

    print(f" Error de formato en fecha: {fecha_str}")
    return None

def convertir_float(valor):
    """Convierte un valor a float, asegurando que solo se convierten números válidos."""
    if not valor or valor.strip().upper() in ["NULL", "R", ""]:
        return None  
    
    try:
        return float(valor)
    except ValueError:
        print(f" Error de conversión en valor flotante: {valor}")
        return None

def importar_viajes():
    """Importa registros desde un CSV y los guarda en la base de datos."""
    if not os.path.exists(FILE_PATH):
        print(f"Error: No se encontró el archivo {FILE_PATH}")
        return

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        batch = []
        total_importados = 0
        errores = 0

        for i, row in enumerate(reader, start=1):
            try:
                trip = Trip(
                    gps_provider=row.get("GpsProvider", ""),
                    booking_id=row.get("BookingID", ""),
                    market_regular=row.get("Market_Regular", ""),
                    booking_id_date=convertir_fecha(row.get("BookingID_Date")),
                    vehicle_no=row.get("vehicle_no", ""),
                    origin_location=row.get("Origin_Location", ""),
                    destination_location=row.get("Destination_Location", ""),
                    org_lat_lon=row.get("Org_lat_lon", ""),
                    des_lat_lon=row.get("Des_lat_lon", ""),
                    data_ping_time=convertir_fecha(row.get("Data_Ping_time")),
                    planned_eta=convertir_fecha(row.get("Planned_ETA")),
                    current_location=row.get("Current_Location", ""),
                    destination_location_actual=row.get("DestinationLocation", ""),
                    actual_eta=convertir_fecha(row.get("actual_eta")),
                    curr_lat=convertir_float(row.get("Curr_lat")),
                    curr_lon=convertir_float(row.get("Curr_lon")),
                    ontime=row.get("ontime", "").strip().lower() == "true",
                    delay=row.get("delay", "").strip(),
                    origin_location_code=row.get("OriginLocation_Code", ""),
                    destination_location_code=row.get("DestinationLocation_Code", ""),
                    trip_start_date=convertir_fecha(row.get("trip_start_date")),
                    trip_end_date=convertir_fecha(row.get("trip_end_date")),
                    transportation_distance_in_km=int(row.get("TRANSPORTATION_DISTANCE_IN_KM", "0")) if row.get("TRANSPORTATION_DISTANCE_IN_KM") else None,
                    vehicle_type=row.get("vehicleType", ""),
                    minimum_kms_to_be_covered_in_a_day=row.get("Minimum_kms_to_be_covered_in_a_day", ""),
                    driver_name=row.get("Driver_Name", ""),
                    driver_mobile_no=row.get("Driver_MobileNo", ""),
                    customer_id=row.get("customerID", ""),
                    customer_name_code=row.get("customerNameCode", ""),
                    supplier_id=row.get("supplierID", ""),
                    supplier_name_code=row.get("supplierNameCode", ""),
                    material_shipped=row.get("Material_Shipped", ""),
                )

                batch.append(trip)
                total_importados += 1

                if len(batch) >= 500:  # Guardar en la BD cada 500 registros
                    with transaction.atomic():
                        Trip.objects.bulk_create(batch, ignore_conflicts=True)
                    batch.clear()

            except Exception as e:
                errores += 1
                print(f" Error en la fila {i}: {e}")

        if batch:
            with transaction.atomic():
                Trip.objects.bulk_create(batch, ignore_conflicts=True)

    print(f"\n Proceso completado: Se importaron {total_importados} registros. Fallaron {errores}.")

if __name__ == "__main__":
    importar_viajes()
    
def limpiar_monto(monto):
    if not monto:  
        return 0
    return float(monto.replace("$", "").replace(",", "").strip())    
    
FILE_PATH1 = os.path.expanduser("~/Escritorio/repo/basesdedatos3/apirest/apirest/DatosPublicos.csv")   
def importar_envios():
    if not os.path.exists(FILE_PATH1):
        print(f"Error: No se encontró el archivo {FILE_PATH1}")
        return

    with open(FILE_PATH1, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        envios = []
        total_importados = 0

        for row in reader:
            try:
                envio = Envio(
                    periodo=row["PERIODO"],
                    proveedor=row["PROVEEDOR"],
                    direccion=row["DIRECCION"],
                    rango_peso_envio=row["RANGO_PESO_ENVIO"],
                    ambito=row["AMBITO"],
                    tipo_envio=row["TIPO_ENVIO"],
                    tipo_servicio=row["TIPO_SERVICIO"],
                    ingresos=limpiar_monto((row["INGRESOS"])),
                    numero_total_envios=int(row["NUMERO_TOTAL_ENVIOS"])
                )

                envios.append(envio)
                total_importados += 1

                # Guardar en la BD cada 500 registros para optimizar memoria
                if len(envios) >= 500:
                    Envio.objects.bulk_create(envios)
                    envios.clear()

            except Exception as e:
                print(f"Error en la fila {total_importados + 1}: {e}")

        # Insertar los últimos registros
        if envios:
            Envio.objects.bulk_create(envios)

        print(f"\nProceso completado: Se importaron {total_importados} registros.")

if __name__ == "__main__":
    importar_envios()
