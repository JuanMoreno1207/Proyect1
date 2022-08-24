from random import shuffle


# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle intento
def probar_suerte():
    intento = 0
    while intento not in range(1, len(palitos)+1):
        intento = int(input(f"Elige un numero del 1 al {len(palitos)}: "))
    else:
        return int(intento)


# Comprobar intento

def chequear_intento(lista, intento):
    print(f"Te ha tocado el palito {lista[intento - 1]}")
    if lista[intento - 1] == '-':
        print("¡Perdiste, a lavar la loza!")
        return False
    else:
        print("¡Salvado!\n")
        item = intento - 1
        palitos.pop(item)
        return True


# Lista inicial
palitos = ['-', '--', '---', '----']


def jugar():
    while len(palitos) > 0:
        if len(palitos) == 1:
            print('Se termino el juego, el siguiente jugador debe lavar la loza')
            break
        else:
            palitos_mezclados = mezclar(palitos)
            print(palitos_mezclados)
            numerousuario = probar_suerte()
            resultado = chequear_intento(palitos_mezclados, numerousuario)
            if resultado:
                continue
            else:
                break


jugar()
