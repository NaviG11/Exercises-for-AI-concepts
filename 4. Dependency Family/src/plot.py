import matplotlib.pyplot as plt

# Definir los hechos de la familia
hechos_familia = [
    ("padre", ("Juan", "Carlos"), ("Juan", "Sofia")),
    ("madre", ("Juana", "Carlos"), ("Juana", "Sofia")),
    ("hermano", ("Carlos", "Sofia")),
    ("padre", ("Carlos", "Ivan"), ("Carlos", "Yhose")),
    ("madre", ("Graciela", "Ivan"), ("Graciela", "Yhose")),
    ("hermano", ("Ivan", "Yhose")),
    ("padre", ("Franz", "Ivar")),
    ("madre", ("Sofia", "Ivar"))
]

# Convertir los hechos en un diccionario de relaciones familiares
familia = {}
for hecho in hechos_familia:
    relacion, *parejas = hecho
    for pareja in parejas:
        if pareja[0] not in familia:
            familia[pareja[0]] = []
        familia[pareja[0]].append((pareja[1], relacion))

# Función para dibujar el árbol
def dibujar_arbol(arbol, padre, nivel, pos):
    hijos = arbol.get(padre, [])
    ancho = 1.0 / (len(hijos) + 1)
    for i, (hijo, relacion) in enumerate(hijos):
        hijo_pos = (nivel * ancho + i * ancho, -nivel)
        pos[hijo] = hijo_pos
        plt.text(hijo_pos[0], hijo_pos[1], hijo, ha='center', va='center')
        plt.plot([pos[padre][0], hijo_pos[0]], [pos[padre][1], hijo_pos[1]], 'k-')
        dibujar_arbol(arbol, hijo, nivel + 1, pos)

# Configurar el gráfico
plt.figure(figsize=(8, 6))
plt.title("Árbol Genealógico Familiar")

# Dibujar el árbol
posiciones = {"Juan": (0.5, 0)}
dibujar_arbol(familia, "Juan", 1, posiciones)

# Establecer límites del eje y revertir el eje y para que la raíz esté en la parte superior
plt.ylim(-4, 1)
plt.gca().invert_yaxis()

# Ocultar ejes
plt.axis('off')

# Mostrar el gráfico
plt.show()
