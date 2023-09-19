import pandas as pd

archivo_csv = 'playlist limpio.csv'
data = pd.read_csv(archivo_csv)
columna_datos = data['track_popularity']

minimo = columna_datos.min()
maximo = columna_datos.max()
media = columna_datos.mean()

print("Funcion agregacion para la popularidad de cada cancion:")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Media: {media}")
