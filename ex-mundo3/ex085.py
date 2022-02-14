temp = [[], []]
valor = 0
for p in range(1, 8):
    valor = int(input(f'Digite o {p}° valor: '))
    if valor % 2 == 0:
        temp[0].append(valor)
    else:
        temp[1].append(valor)
print(f'Os pares são {sorted(temp[0])}.')
print(f'Os ímpares são {sorted(temp[1])}.')
