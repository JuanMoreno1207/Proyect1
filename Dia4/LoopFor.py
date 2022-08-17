lista = ['a','b','c']
for item in lista:
    numero_letra = lista.index(item) + 1
    print(f'Letra: {item} Indice: {numero_letra}')

lista = ['pablo','laura','fede','luis','julia']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)

# Iterar en listas
for a,b in [[1,2],[2,3],[5,6]]:
    print(a)

# Iterar en Diccionario
dic = {'Clave1':'a','Clave2':'b','Clave3':'c'}
for item in dic:
    print(item)
# Imprime por defecto las llaves

for llave, valor in dic.items():
    print(llave + valor)
# Imprime las llaves y valor puesto que trae el dic en forma de tuplas

for item in dic.values():
    print(item)
# Imprime unicamente los valores

lista = [1,5,8,7,9,6,5,4,7,9,6]
suma = 0
for numeros in lista:
    suma = numeros + suma
print(suma)

# Sumar valores pares e impares
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
