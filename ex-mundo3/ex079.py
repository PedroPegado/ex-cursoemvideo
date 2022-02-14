valor = []
while True:
    x = (int(input('Digite um valor: ')))
    if x not in valor:
        valor.append(x)
        print('Prontinho, adicionado com sucesso. :)')
    else:
        print('Valor duplicado, não vou adicionar. :(')

    y = str(input('quer continuar ? S ou N? ')).strip().upper()[0]
    if y in 'Nn':
        break
print(f'os números cadastrados foram {sorted(valor)}')



