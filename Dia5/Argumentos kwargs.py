def suma (num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg es igual a : {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


# suma(15,50,100,200,300,400,x='Uno',y='Dos',z='Tres')

def cantidad_atributos(**kwargs):
    suma = 0
    for kw in kwargs:
        suma += 1
    return suma


def lista_atributos(**kwargs):
    lista = list()
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista

def describir_persona(nombre,**kwargs):
    print(f"Caracteristicas de {nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# describir_persona("María", color_ojos="azules", color_pelo="rubio")


