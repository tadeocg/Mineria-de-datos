import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

archivo_csv = 'playlist limpio.csv'
df = pd.read_csv(archivo_csv, parse_dates=['album_release_date'], index_col='album_release_date')

# Visualizar los datos
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['track_popularity'], label='Datos originales')  # Cambia 'tu_columna_de_datos'
plt.title('Datos de canciones')
plt.xlabel('Fecha')
plt.ylabel('Número de reproducciones')
plt.legend()
plt.show()

# Aplicar el modelo de forecasting (Holt-Winters Exponential Smoothing)
modelo = ExponentialSmoothing(df['track_popularity'], seasonal='add', seasonal_periods=12)
resultado = modelo.fit()

# Realizar la predicción para los próximos N pasos
N = 5
prediccion = resultado.forecast(steps=N)

# Visualizar los resultados
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['track_popularity'], label='Datos originales')
plt.plot(pd.date_range(start=df.index[-1], periods=N + 1, freq=df.index.freq)[1:], prediccion, label='Predicción')
plt.title('Forecasting de canciones')
plt.xlabel('Fecha')
plt.ylabel('Número de reproducciones')
plt.legend()
plt.show()
