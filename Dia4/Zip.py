# funcion que nos sirve para combinar una lista y crear una lista de Tuples
nombres = ['Ana','Juan','Hugo']
edades = [65,29,42]
ciudades = ['Lima','Bogota','Mexico']
combi = list(zip(nombres, edades, ciudades))
# print(combi)
for nombre, edad, ciudad in combi:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
