def contar_primos(num1):
    cantidad = 0
    rango = list(range(2, num1+1))
    for n in rango:
        if not num1 % n == 0:
            print('Suma')
            print(num1 % n)
            cantidad += 1
    return cantidad




print(contar_primos(29))