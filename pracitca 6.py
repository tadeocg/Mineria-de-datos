import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

archivo_csv = 'playlist limpio.csv'
data = pd.read_csv(archivo_csv, parse_dates=['album_release_date'])

X = data['album_release_date']
y = data['track_popularity']

X_numeric = mdates.date2num(X)

X_train, X_test, y_train, y_test = train_test_split(X_numeric, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train.reshape(-1, 1), y_train)

y_pred = modelo.predict(X_test.reshape(-1, 1))

plt.scatter(X_test, y_test, color='black', label='Datos reales')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regresión lineal')
plt.xlabel('album_release_date')
plt.ylabel('track_popularity')
plt.title('Regresión Lineal por Fecha')
plt.legend()
plt.show()

print("Coeficiente (pendiente):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
