import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import seaborn as sns
import matplotlib.pyplot as plt

archivo_csv = 'playlist limpio.csv'
data = pd.read_csv(archivo_csv)

modelo = ols('track_duration_ms ~ track_popularity', data=data).fit()

anova_resultados = anova_lm(modelo)

print("Resultados del ANOVA:")
print(anova_resultados)

sns.catplot(x='track_popularity', y='track_duration_ms', data=data, kind='box')
plt.title('Gráfico de Cajas por popularidad')
plt.show()
