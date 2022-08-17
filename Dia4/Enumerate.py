lista = ['a','b','c']
# Enumerate crea un indice ordenado por cada elemento de la lista iterable
for indice,item in enumerate(lista):
    print(indice, item)

# Crear lista con indice de cada caracter de la palabra

palabra = "Python"
lista_indices = []
for indices in enumerate(palabra):
    lista_indices.append(indices)

# Enumerar la lista y despues imprimir unicamente los indices de los nombres que comiencen con M
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)
    else:
        continue

