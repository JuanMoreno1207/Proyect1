# Elementos mutables
# Declarar tipo lista
mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']
# print(mi_lista)
# Concatenar listas
print(mi_lista + mi_lista2)
# Agregar elemento a lista
mi_lista2.append('g')
print(mi_lista2)
# Quitar elemento a lista
# por defecto elimina el ultimo elemento, debe ir el indice
# Se puede recuperar el valor eliminado asignado el pop a una variable
mi_lista2.pop(0)
print(mi_lista2)
# Ordenar elementos de una lista con el metodo sort(), metodo que no retorna respuesta por ende
# NO se puede asignar
lista_3 = ['z','p','a','f']
lista_3.sort()
lista_3.reverse()
# reverse () funciona de la misma manera pero en orden contrario
print(lista_3)