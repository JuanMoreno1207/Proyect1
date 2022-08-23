from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle intento
def probar_suerte():
    intento = ''
    print(len(palitos))
    while intento not in range(0, len(palitos)):
        intento = input(f"Elige un numero del 1 al {len(palitos)}: ")
        if intento < len(palitos):
            return intento
        else:
            print('pasa')

# Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("¡Perdiste, a lavar la loza!")
    else:
        print("¡Salvado!")
        palo = lista[intento - 1]
        palitos.remove(palo)
    print(f"Te ha tocado el palito {palo}")


def juego():
    print('A jugarleee')
    palitos_mezclados = mezclar(palitos)
    seleccion = probar_suerte()
    print('salio')
    # chequear_intento(palitos_mezclados, seleccion)



juego()


