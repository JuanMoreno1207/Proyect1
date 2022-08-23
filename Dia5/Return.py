def multiplicar(num1, num2):
    return num1 * num2


# Llamar y asignar funcion
resultado = multiplicar(2, 2)
print(resultado)

palabra = 'Juan'


def invertir_palabra(palabra):
    lista = list(palabra)
    lista.reverse()
    TextoStr = "".join(lista).upper()
    return TextoStr


print(invertir_palabra(palabra))
