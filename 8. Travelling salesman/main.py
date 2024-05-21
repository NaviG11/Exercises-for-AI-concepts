import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

# Crear un grafo completo con 8 nodos
G = nx.complete_graph(8)

# Dibujar el grafo
pos = nx.spring_layout(G)  # Posición de los nodos en el dibujo
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold", edge_color="gray")
plt.title("Grafo Completo con 8 Nodos")
plt.show()

# Listar todos los nodos del grafo
nodes = list(G.nodes)

# Obtener todas las permutaciones posibles de los nodos para los caminos
all_possible_paths = list(permutations(nodes))

# Imprimir la cantidad de caminos posibles (8!)
print(f"Cantidad de caminos posibles: {len(all_possible_paths)}")

# Opcional: Imprimir algunas permutaciones (por ejemplo, las primeras 5)
print("Algunos caminos posibles:")
for path in all_possible_paths[:5]:
    print(path)

# Guardar las combinaciones en un archivo de texto (opcional)
with open('all_possible_paths.txt', 'w') as f:
    for path in all_possible_paths:
        f.write(f"{path}\n")
