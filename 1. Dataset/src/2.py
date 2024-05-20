import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
datos = pd.read_csv("../../data/StressLevelDataset.csv")

# Eliminar cualquier columna no numérica que pueda haber en los datos
datos = datos.select_dtypes(include=[np.number])

# Seleccionar la última columna
ultima_columna = datos.iloc[:, -1]

# Filtrar los valores 0, 1 y 2
valores_filtrados = ultima_columna[ultima_columna.isin([0, 1, 2])]

# Calcular el tercer cuartil (Q3) y el percentil 80 utilizando NumPy
ultimo_cuartil = np.percentile(valores_filtrados, 75)
percentil_80 = np.percentile(valores_filtrados, 80)

print("Último cuartil (Q3):", ultimo_cuartil)
print("Percentil 80:", percentil_80)

# Graficar los datos utilizando seaborn
plt.figure(figsize=(8, 6))
sns.histplot(valores_filtrados, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(x=ultimo_cuartil, color='red', linestyle='--', label='Último cuartil (Q3)')
plt.axvline(x=percentil_80, color='green', linestyle='--', label='Percentil 80')
plt.title('Histograma de la Última Columna (valores 0, 1, 2) con Último Cuartil y Percentil 80')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.show()
