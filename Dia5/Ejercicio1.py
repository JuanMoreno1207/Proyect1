def devolver_distintos(n1,n2,n3):
    lista = [n1,n2,n3]
    suma = sum(lista)
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    elif suma in range(10,16):
        lista.sort()
        return lista[1]

# print(devolver_distintos(5,6,3))