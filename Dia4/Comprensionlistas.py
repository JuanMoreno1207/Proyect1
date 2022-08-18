lista = [pr for pr in 'Python']
print(lista)
lista = [n for n in range(0,5)]
print(lista)
lista = [n if n*2 > 10 else 'no' for n in range(0,21)]
print(lista)

pies = [10,20,30,40,50]
metros = [pie*3.281 for pie in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [valor for valor in valores if valor % 2 == 0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grado-32)*(5/9) for grado in temperatura_fahrenheit]
print(grados_celsius)
