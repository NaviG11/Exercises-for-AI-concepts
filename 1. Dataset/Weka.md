# Weka

El paquete de Weka contine una colección de herramientas de visualización y algoritmos para análisis de datos y modelado predictivo, unidos a una interfaz gráfica de usuarioi para acceder fácilmente a sus funcionalidades. La versión original de Weka fue un front-end en TCL/TK para modelar algoritmos implementados en otros lenguajes de programación, más unas utilidades para preprocesamiento de datos desarrolladas en C para hacer experimentos de aprendizaje automático. Esta verión original de diseño inicialemente como herramienta para analizar datos procedentes del dominio de la agricultura, pero la verión más reciente basada en Java, que empezó a desarrollarse en 1997, se utiliza en muchas y muy diferentes áreas, en particular con finalidades educativas y de investigación.

## Características

Weka soporta varias tareas estándar de minería de datos, especialmente preprocesamiento de datos, clustering, clasificación, regresión, visualización y selección.

- Fichero plano (flat file)
- Acceso a base de datos vía SQL (con JDBC)
- Modelado de secuencias, por ejemplo, para predecir el próximo evento en una secuencia

## Explorer

- Panel Preprocess: importar datos, y para procesar estos datos utilizando los denominados algoritmos de filtrado.
- Panel Classify: permite al usuario aplicar algoritmos de clasificación estadística y análisis de regresión a los conjuntos de datos resultantes.
- Panel Associate: proporciona acceso a las reglas de asociación aprendidas que intentan identificar todas las interrelaciones importantes entre los atributos de los datos.
- Panel Cluster: da acceso a las técnicas de clustering o agrupamiento de Weka como por ejemplo el algoritmo k-means.
- Panel Select Attributes: proporciona métodos para seleccionar los atributos más relevantes de un conjunto de datos.
- Panel Visualize: muestra una matriz de puntos dispersos (scatterplot) donde cada punto individual puede seleccionarse y agrandarse para ver más detalles.

## Knowledge Flow

Flujo de conocimiento es una interfaz que en esencia implementa las mismas funciones que Explorer, y además permite "arrastrar y soltar".
