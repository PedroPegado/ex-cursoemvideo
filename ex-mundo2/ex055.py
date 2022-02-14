maior = 0
menor = 0
for balanca in range(1, 6):
    x = float(input(f'Qual é o peso da {balanca}° pessoa? '))
    if balanca == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
print(f'O mais pesado pesado tem {maior}Kg e o mais leve tem {menor}Kg')


