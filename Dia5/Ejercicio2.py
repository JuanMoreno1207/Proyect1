def palabra_rota(palabra):
    conj = set(palabra)
    lista = list(conj)
    lista.sort()
    print(lista)

palabrarota('entretenido')