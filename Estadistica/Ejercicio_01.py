# EJERCICIO 1

# Dada estos valores: 15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16

# 1) Realiza un Histograma con tamaño de barra 2.

# 2) ¿Cuál es el número que más se repite?

# 3) ¿Qué pasa si cambiamos a tamaño de barra 5?

# 4) ¿Qué pasa si cambiamos a tamaño de barra 20?

# 5) ¿Qué parece indicar el sesgo en la distribución?

from unicodedata import numeric
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm 



lista = '15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16'
lista = lista.split(' ')
valores = []
for i in lista:
    valores.append(int(i))

df = pd.DataFrame({'Valores': valores})

fig = plt.figure(figsize=(12,8))

ax1 = plt.subplot(2,2,1)
ax1.hist(df['Valores'], bins = 2, histtype = 'bar', label='Tamaño 2', rwidth=0.75)
plt.title('Histograma de frecuencia')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
# plt.show()

ax2 = plt.subplot(2,2,2)
ax2.hist(df['Valores'], bins = 5, histtype = 'bar', label='Tamaño 5')
plt.title('Histograma de frecuencia')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
# # plt.show()

ax3 = plt.subplot(2,2,3)
ax3.hist(df['Valores'], bins = 20, histtype = 'bar', label='Tamaño 20')
plt.title('Histograma de frecuencia')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
# plt.show()

# valores de la media (mu) y desviación típica (sigma) de los datos
mu, sigma = stats.norm.fit(df.Valores)
x_hat = np.linspace(min(df.Valores), max(df.Valores), num=100)
y_hat = stats.norm.pdf(x_hat, mu, sigma)
# Gráfico
ax4 = plt.subplot(2,2,4)
ax4.plot(x_hat, y_hat, linewidth=2, label="normal")
# ax.hist(x=notas_1, density=True, bins=30, color="#3182bd", alpha=0.5)
ax4.plot(df.Valores, np.full_like(df.Valores, -0.01), "|k", markeredgewidth=1)
plt.title("Distribución df.Valores")
plt.xlabel("Valores")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()

moda = df.Valores.mode()
print(f'El valor {moda.iloc[0]} que más se repite')
