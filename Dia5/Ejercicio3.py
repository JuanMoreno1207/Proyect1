def valida_cero(*args):
    cantidad = ''
    for arg in args:
        if arg == 0 and cantidad == '1':
            return True
        elif arg == 0 and cantidad == '':
            cantidad = '1'
        elif arg != 0:
            cantidad = ''
    return False


# print(valida_cero(5,6,1,0,0,9,3,5))