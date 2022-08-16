mi_texto = str(input('Escribe tu texto, por favor : ')).lower()
mis_letras = list(input('Escribe 3 letras, por favor : ').lower())

cantidad1 = mi_texto.count(mis_letras[0])
cantidad2 = mi_texto.count(mis_letras[1])
cantidad3 = mi_texto.count(mis_letras[2])
cantidadP = mi_texto.split()
fragmento1 = mi_texto[0]
fragmento2 = mi_texto[-1]
Textoalrev = list(mi_texto)
Textoalrev.reverse()
TextoStr = "".join(Textoalrev)
Existe = ("python" in mi_texto)
diccionario = {True: 'Si', False: 'No'}
print(f"La letra {mis_letras[0]} aparece {cantidad1} veces en el texto")
print(f"La letra {mis_letras[1]} aparece {cantidad2} veces en el texto")
print(f"La letra {mis_letras[2]} aparece {cantidad3} veces en el texto")
print(f"El texto tiene {len(cantidadP)} palabras")
print(f"La primera letra del texto es {fragmento1} y la ultima es {fragmento2}")
print(f"El texto al reves da como resultado : {TextoStr}")
print(f"La palabra python {diccionario[Existe]} existe en el texto")

