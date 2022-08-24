def suma_cuadrados(*args):
    suma = 0
    for n in args:
        suma += n ** 2
    return suma

# El signo * permite ingresar x cantidad de argumentos y en este caso sumarlos uno a uno elevendolo a la raiz cuadrada