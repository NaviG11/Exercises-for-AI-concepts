import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Paso 1: Cargar el dataset
df = pd.read_csv('../data/StressLevelDataset.csv')

# Paso 2: Preprocesar los datos (codificar variables categóricas)
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Separar características y etiquetas
X = df.drop('mental_health_history', axis=1)
y = df['mental_health_history']

# Paso 3: Crear y entrenar el modelo de árbol de decisión
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Paso 4: Graficar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=['No', 'Sí'])
plt.show()
