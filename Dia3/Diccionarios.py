# Se declara con corchetes y cada llave-valor se separa por coma
diccionario = {'c1': 'Valor1', 'c2': 'valor2'}
# print(type(diccionario))
# Acceder algun valor por su llave
resultado = diccionario['c1']
# print(resultado)
Cliente = {'nombre': 'Juan', 'apellido': 'Moreno', 'peso': 80, 'altura': 1.83}
# print(Cliente['altura'])
dic = {'c1': ['a','b','c'], 'c2': ['d','e','f']}
# print(dic['c2'][1].upper())
# Agregar elemento a diccionario ya creado, en caso de que la llave NO exista, la creo o la remplaza
Cliente['Ciudad'] = 'Bogota D.C.'
print(Cliente)
# Traer las llaves de un diccionario
print(Cliente.keys())
# Traer los valores de un diccionario
print(Cliente.values())
# Traer los items del diccionario
print(Cliente.items())


