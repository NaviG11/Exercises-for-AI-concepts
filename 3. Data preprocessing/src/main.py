import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
datos = pd.read_csv("../data/StressLevelDataset.csv")

# Use preprocessing algorithms to clean the data

# Clean data with replacement of missing values
data = datos['extracurricular_activities']
print(data)
print("1. Se reemplaza los datos faltantes por la media, para evitar campos vacios en la columna")
datos['extracurricular_activities'].fillna(datos['extracurricular_activities'].mean(), inplace=True)
print(data)

#2th
print("\n\n· 2. Eliminacion de columnas:")

print(datos)

datos = datos.drop("mental_health_history", axis=1)
datos = datos.drop("teacher_student_relationship", axis=1)
print("Se eliminan algunas columnasque aportan poco en el analisis de datos")
print(datos)

#3th with breathing problems
print("\n\n· 3. NORMALIZACION. en la columna extracurricular_activities :")


# Crea el objeto MinMaxScaler
scaler = MinMaxScaler()

print("Normalizando los datos para tenerlo en una escala de 0 a 1")
datos['extracurricular_activities'] = scaler.fit_transform(datos['extracurricular_activities'].values.reshape(-1, 1))
print(datos)

#4th One hot encoding
# from sklearn.preprocessing import OneHotEncoder
# dataset = pd.read_csv("../data/StressLevelDataset.csv")
# print("\n\n· 4. One hot encoding en la columna anxiety_level:")
# columna_a_codificar = dataset["anxiety_level"]
# encoder = OneHotEncoder(handle_unknown="ignore")
# encoder.fit(columna_a_codificar.values.reshape(-1, 1))
# columna_codificada = encoder.transform(columna_a_codificar.values.reshape(-1, 1))
# columna_codificada_df = pd.DataFrame(columna_codificada, columns=encoder.get_feature_names_out())
# dataset = pd.concat([dataset, columna_codificada_df], axis=1)

#5th Escalado de datos
from sklearn.preprocessing import StandardScaler
datos = pd.read_csv("../data/StressLevelDataset.csv")
columna_a_escalar = datos["anxiety_level"]
scaler = StandardScaler()
scaler.fit(columna_a_escalar.values.reshape(-1, 1))
columna_escalada = scaler.transform(columna_a_escalar.values.reshape(-1, 1))
datos["anxiety_level_escalada"] = columna_escalada

# -1 : debajo de la media
# 0 : media
# 1 : por encima de la media