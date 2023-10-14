import pandas as pd
import matplotlib.pyplot as plt

archivo_csv = 'playlist limpio.csv'
data = pd.read_csv(archivo_csv, parse_dates=['album_release_date'])

datos_agrupados = data.groupby(data['album_release_date'].dt.month)['number_of_tracks_in_album'].sum()

plt.figure(figsize=(10, 6))
datos_agrupados.plot(kind='bar', color='skyblue')

plt.title('Gráfico de Barras por Mes de canciones por album')
plt.xlabel('Mes')
plt.ylabel('Suma de canciones')
plt.xticks(rotation=0)
plt.grid(axis='y')

plt.show()
