import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("../data/StressLevelDataset.csv")
# Eliminar cualquier columna no numérica que pueda haber en los datos
datos = datos.select_dtypes(include=[np.number])

# Calcular el último cuartil y el percentil 80 utilizando NumPy
ultimo_cuartil = np.percentile(datos, 75)
percentil_80 = np.percentile(datos, 80)

print("Último cuartil (Q3):", ultimo_cuartil)
print("Percentil 80:", percentil_80)

# Graficar los datos
# Histograma
plt.figure(figsize=(8, 6))
plt.hist(datos.values.flatten(), bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(x=ultimo_cuartil, color='red', linestyle='--', label='Último cuartil (Q3)')
plt.axvline(x=percentil_80, color='green', linestyle='--', label='Percentil 80')
plt.title('Histograma de Datos con Último Cuartil y Percentil 80')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.show()