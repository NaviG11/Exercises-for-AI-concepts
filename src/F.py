import csv
def frecuencias_acumuladas(archivo_csv):
  """
  Calcula las frecuencias acumuladas de cada clase en cada columna de un archivo CSV.
  Argumentos:
    archivo_csv (str): Ruta del archivo CSV.
  Devuelve:
    dict: Diccionario donde las claves son las tuplas (nombre_columna, clase) y los valores son las frecuencias acumuladas.
  """
  frecuencias = {}
  with open(archivo_csv, 'r') as csvfile:
    lector_csv = csv.reader(csvfile)
    # Obtiene los nombres de las columnas
    nombres_columnas = next(lector_csv)
    for fila in lector_csv:
      # Recorre cada fila del CSV
      for i, valor in enumerate(fila):
        # Obtiene la clave (nombre_columna, clase)
        clave = (nombres_columnas[i], valor)
        # Inicializa la frecuencia acumulada si no existe
        if clave not in frecuencias:
          frecuencias[clave] = 0
        # Incrementa la frecuencia acumulada
        frecuencias[clave] += 1
  return frecuencias

# Ejemplo de uso
archivo_csv = '../data/StressLevelDataset.csv'
frecuencias_acumuladas = frecuencias_acumuladas(archivo_csv)
# Imprime las frecuencias acumuladas
for clave, frecuencia in frecuencias_acumuladas.items():
  print(f"{clave}: {frecuencia}")
