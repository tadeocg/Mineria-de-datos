import pandas as pd
from tabulate import tabulate

archivo_csv = 'playlist limpio.csv'
data = pd.read_csv(archivo_csv)

columna_1 = data['track_duration_ms']
columna_2 = data['track_popularity']

estadisticas_columna_1 = {
    'Media': columna_1.mean(),
    'Mediana': columna_1.median(),
    'Mínimo': columna_1.min(),
    'Máximo': columna_1.max()
}

estadisticas_columna_2 = {
    'Media': columna_2.mean(),
    'Mediana': columna_2.median(),
    'Mínimo': columna_2.min(),
    'Máximo': columna_2.max()
}

print("Estadísticas descriptivas para 'Duracion de canciones en ms':")
print(tabulate(estadisticas_columna_1.items(), headers=['Estadística', 'Duracion'], tablefmt='fancy_grid'))

print("\nEstadísticas descriptivas para 'Popularidad de canciones':")
print(tabulate(estadisticas_columna_2.items(), headers=['Estadística', 'Popularidad'], tablefmt='fancy_grid'))