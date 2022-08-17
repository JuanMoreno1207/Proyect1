# El primer valor es de donde inicia, el segundo no es inclusivo y es hasta donde va y el tercero es la cantida de pasos en cada flujo
for numero in range(0,4,2):
    print(numero)

mi_lista = list(range(1,16))
suma_cuadrados = 0
for numero in mi_lista:
    suma_cuadrados += numero**2
print(suma_cuadrados)