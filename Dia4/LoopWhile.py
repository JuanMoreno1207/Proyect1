monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("Se acabaron las monedas")

respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n): ")
else:
    print('Gracias')

# pass, no hacer nada, fluir dentron del while sin problema
# break, Interrumpe el flujo y no hace nada mas
# continue, salta el ciclo del flujo donde se declare

# Pintar unicamente los numeros divisibles por 5, cuando no se cumpla dicha condicion no imprimir
numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
        continue

# Interrumpir flujo cuando encuentre numero negativo
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if(numero < 0):
        break
    else:
        print(numero)



