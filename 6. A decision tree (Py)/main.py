import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

# Cargar el dataset
iris = load_iris()
X = iris.data
y = iris.target

# Crear y entrenar el modelo de árbol de decisión
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Graficar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()
