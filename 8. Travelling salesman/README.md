# 8

Selecciones un grafo del **AGENTE**-**VIAJERO** con al menos "**8 nodos**", de los cuales obtenga todos los posibles caminos con Python (no solucione, solo obtenga todas las combinaciones) [check sample avoid repeats data].

Importaciones:
networkx se utiliza para crear y manejar el grafo.
itertools.permutations se usa para generar todas las permutaciones posibles de los nodos.

Creación del grafo:
nx.complete_graph(8) crea un grafo completo con 8 nodos, es decir, un grafo donde cada nodo está conectado con todos los demás nodos.

    Listar los nodos:
        nodes = list(G.nodes) obtiene la lista de nodos del grafo.

    Generar todas las permutaciones:
        all_possible_paths = list(permutations(nodes)) genera todas las permutaciones posibles de los nodos, que representan todos los caminos posibles que el agente viajero puede tomar.

    Impresión de resultados:
        Se imprime la cantidad total de caminos posibles (8! = 40320).
        Se imprimen algunas de las permutaciones para dar una idea de los caminos generados.

    Guardar en un archivo (opcional):
        Se guardan todas las combinaciones en un archivo de texto all_possible_paths.txt para su posterior análisis.
