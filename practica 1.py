import requests

url = "https://download937.mediafire.com/g36ewq8bvcagk-PLaCD0WMdZl1F8_6_3jEHdctKRTT3sMSX--lZLCMshZtO57sG2YKzullf-r8YuOTi_ATvXD-5xErjIuk9S6VJ0TTAWRcEZrM1RSOf2VYkIasiSwZIbx5ji9C5PcXORIRuPUdiLl1KK1Y5y2IOc2gUqD7xVohVS69I/70wph81oum8fenm/playlist.csv"

nombre_archivo_local = "playlist.csv"

response = requests.get(url)

if response.status_code == 200:
    with open(nombre_archivo_local, 'wb') as archivo:
        archivo.write(response.content)
    print(f"Archivo CSV descargado como {nombre_archivo_local}")
else:
    print("Error al descargar el archivo CSV")