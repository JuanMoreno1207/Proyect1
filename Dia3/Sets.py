# Declarar Sets, no permite valores duplicados e igualmente no nos ordenados ni mutables
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
mi_set2 = {2,4,6,8}
print(type(mi_set2))
print(mi_set2)

# Buscar elemento usando el metodo in
print( 2 in mi_set2)

# Unir sets .union()
mi_set3 = mi_set.union(mi_set2)
print(mi_set3)

# Agregar al conjunto .add
mi_set3.add(15)
print(mi_set3)

# Eliminar elemento .remove() o discard() para evitar error si no existe
mi_set3.remove(15)
print(mi_set3)

# Eliminar elemento aleatorio con pop()
mi_set3.pop()
print(mi_set3)

# Limpiar conjunto clear()
mi_set3.clear()
print(mi_set3)

