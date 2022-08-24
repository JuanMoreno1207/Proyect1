from random import *


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    return


valor1, valor2 = lanzar_dados()
# print(valor1, valor2)
resultado = evaluar_jugada(valor1, valor2)
# print(resultado)

# Ejercicio2
lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista_num):
    conj = set(lista_num)
    lists = list(conj)
    lists.sort()
    lists.pop()
    return lists


def promedio(lista_promedio):
    suma = 0
    for n in lista_promedio:
        suma += n
    prom = suma / len(lista_promedio)
    return prom


# Ejercicio 3
lista_numeros =list(range(0, 11))


def lanzar_moneda():
    moneda =['Cara', 'Cruz']
    monedaale = choice(moneda)
    return monedaale


def probar_suerte(moneda, listanum):
    if moneda == 'Cara':
        print("La lista se autodestruirá")
        listanum = []
        return listanum
    else:
        print("La lista fue salvada")
        return listanum

# print(probar_suerte('Cara', lista_numeros))