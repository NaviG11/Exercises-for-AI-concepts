# Este módulo se encarga de leer los datos de un archivo CSV
# y devolverlos en una lista de Python.

def leer_datos(archivo):
  datos = []
  with open(archivo, 'r') as file:
      # Ignorar la primera línea si contiene encabezados
      next(file)
      for linea in file:
          # Suponiendo que los datos están separados por comas
          datos.extend(map(float, linea.strip().split(',')))
      print("==========================")
      print(len(datos))
  return datos
