# Cuartiles

## ¿Qué es un Cuatil y un Percentil?

- Un cuartil son cuantiles que se multiplican por **un cuarto de un conjunto de datos**.
- El cuartil es cada uno de los tres valores que pueden dividir un grupo de números **ordenados** ascendente o descendente, en cuantro partes iguales.
- Cada cuartil determina la separación entre uno y otro subgrupo, dentro de un conjunto de valores estudiados.

El concepto de cuartil es propio de la estadistica descriptiva y es de gran utilidad para el análisis de datos.

- Q1 1re cuartil, deja 25% de las observaciones menores o iguales a él y el 75% superiores a él.
- Q2 2do cuartil, coincide con la mediana, deja 50% de las observaciones menores o iguales a él y el 50% superiores a él.
- Q3 3er cuartil, deja 75% de las observaciones menores o iguales a él y el 25% superiores a él.

Utilizaremos los cuartiles solamente para datos agrupados en intervalos de clase. Las fórmulas para la determinación de los cuartiles Q1, y Q3 son semejantes a la usada para el calculo de la mediana.

## Determinanción de la mediana

1er Paso: Se calcula n/4

2do Paso: Se identifica la clase que contiene a Q1, por medio de las frecuencias acumuladas, esto es, por la desigualdad.

3er Paso: Se aplica la fórmula:
$$
Q_1 = l_{Q_1} + (\frac{\frac{n}{4}-F_{k-1}}{F_k-F_{k-1}}) * C_{Q_1}
$$
ó
$$
Q_1 = l_{Q_1} + (\frac{\frac{1}{4}-H_{k-1}}{H_k-H_{k-1}})* C_{Q_1}
$$
Cuando se usa la frecuencias acumuladas relativas.

$$
a(N + 1)/4
$$
Donde:
a tomara los valores de 1, 2, 3 y N es el número de valores analizados

Tabla de frecuencias acumuladas

$$
Q_a = L_i + \frac{\frac{aN}{4}-F_{i-1}}{f_i} A_i
$$
Donde:
Li es el límite inferior de la clase donde se encuentra el cuartil.
N es la suma de frecuencias absolutas.
F(i-1) es la frecuencia acumulada de la clase anterior.
Ai es la amplitud de la clase, es decir, el número de valores que contine el intervalo.
