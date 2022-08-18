# Importar biblioteca
from random import *

# Integer aleatorio (desde - hasta)
aleatorio = randint(1,50)
# print(aleatorio)

# Decimal aleatorio (desde - hasta)
aleatorio = round(uniform(1,50),1)
# print(aleatorio)

# Numero decimal aleatorio, sin rango de inicio o final
aleatorio = random()
# print(aleatorio)

# Selecciona un valor random sobre un iterable
colores=['Azul','Rojo','Amarillo']
aleatorio = choice(colores)
# print(aleatorio)

# Permite mezclar los elementos de un iterable
shuffle(colores)
# print(colores)