import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Cargar el conjunto de datos desde un archivo CSV
file_path = 'playlist limpio.csv'
data = pd.read_csv(file_path)

# Visualizar las primeras filas del conjunto de datos
print(data.head())

# Seleccionar las columnas para el análisis de regresión
X = data['track_popularity'].values.reshape(-1, 1)
y = data['number_of_tracks_in_album'].values

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular métricas de rendimiento
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = metrics.mean_squared_error(y_test, y_pred, squared=False)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')

# Visualizar el gráfico de dispersión con la línea de regresión
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_test.flatten(), y=y_test, label='Datos reales')
sns.lineplot(x=X_test.flatten(), y=y_pred, color='red', label='Línea de regresión')
plt.title('Análisis de Regresión Lineal')
plt.xlabel('Popularidad')
plt.ylabel('Canciones en el album')
plt.legend()
plt.show()
