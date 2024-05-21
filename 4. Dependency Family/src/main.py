from kanren import Relation, facts, var, run, conde, eq
import networkx as nx
import matplotlib.pyplot as plt
# https://github.com/pythological/kanren
# Definir las relaciones

padre = Relation()
madre = Relation()
hermano = Relation()

# Definir los hechos
facts(padre, ('Juan', 'Carlos'), ('Juan', 'Sofia'))
facts(madre, ('Juana', 'Carlos'), ('Juana', 'Sofia'))
facts(hermano, ('Carlos', 'Sofia'))

facts(padre, ('Carlos', 'Ivan'), ('Carlos', 'Yhose'))
facts(madre, ('Graciela', 'Ivan'), ('Graciela', 'Yhose'))
facts(hermano, ('Ivan', 'Yhose'))

facts(padre, ('Franz', 'Ivar'))
facts(madre, ('Sofia', 'Ivar'))

# Consultar los hijos de Juan
x = var()
resultado = run(0, x, padre('Juan', x))
print("Hijos de Juan:", list(resultado))

resultado = run(0, x, padre('Carlos', x))
print("Hijos de Carlos:", list(resultado))

resultado = run(0, x, padre('Franz', x))
print("Hijos de Franz:", list(resultado))

# Definir la relación de abuelo
abuelo = Relation()

def es_abuelo(abuelo, nieto):
    padre_intermedio = var()
    return conde(
        (padre(abuelo, padre_intermedio), padre(padre_intermedio, nieto)),
        (padre(abuelo, padre_intermedio), madre(padre_intermedio, nieto))
    )

# Consultar si Juan es abuelo de alguien
y = var()
resultado = run(0, y, es_abuelo('Juan', y))
print("Nietos de Juan:", list(resultado)) # No tiene nietos

# Verificar si Yhose es hija de Juan
resultado = run(1, x, padre('Juan', 'Yhose'))
print("Yhose es hija de Juan:", bool(resultado)) # False

# Verificar si Ivan es nieto de Juan
resultado = run(1, x, es_abuelo('Juan', 'Yhose'))
print("Yhose es nieto de Juan:", bool(resultado))

# Verificar si Ivar e Ivan son primos
def es_primo(primo1, primo2):
    padre_primo1 = var()
    padre_primo2 = var()
    return conde(
        # Primer caso: primo1 comparte el mismo padre y primo2 es hijo del mismo padre
        (padre(padre_primo1, primo1), padre(padre_primo2, primo2), hermano(padre_primo1, padre_primo2)),
        # Segundo caso: primo1 es hijo del padre y primo2 es hijo de la madre
        (padre(padre_primo1, primo1), madre(padre_primo2, primo2), hermano(padre_primo1, padre_primo2)),
        # Tercer caso: primo1 es hijo de la madre y primo2 es hijo del padre
        (madre(padre_primo1, primo1), padre(padre_primo2, primo2), hermano(padre_primo1, padre_primo2)),
        # Cuarto caso: primo1 comparte la misma madre y primo2 es hijo de la misma madre
        (madre(padre_primo1, primo1), madre(padre_primo2, primo2), hermano(padre_primo1, padre_primo2))
    )

# Consultar si Ivar e Ivan son primos
resultado = run(1, x, es_primo('Ivar', 'Ivan'))
print("Ivar e Ivan son primos?:", bool(resultado))

print("Fin del programa")
