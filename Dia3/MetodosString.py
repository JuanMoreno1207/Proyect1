texto = "Este es el texto de Juan"
# Pasar a mayusculas
Resultado = texto.upper()
print(Resultado)
# Pasar minusculas
Resultado = texto.lower()
print(Resultado)
# Separar string y convertirlo a lista
Resultado = texto.split()
print(Resultado)
# Unir string .join
a = "Juan"
b = "Bautista"
Resultado = " ".join([a,b])
print(Resultado)
# find, retorna -1 en caso de no encontrar el caracter
Resultado = texto.find("Juan")
print(Resultado)
# replace, remplaza cadena n por cadena v
Resultado = texto.replace("Juan", "Bautista")
print(Resultado)