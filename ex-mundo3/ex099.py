from time import sleep
def maior(* num):
    contador = maior = 0

    print('Analisando essa porra... ')
    sleep(1)

    for i in num:
        if i > maior:
            maior = i
        contador += 1
        print(f'{i}', end=' ')
    print()
    if contador == 0:
        print('Não haviam números para serem analisados.')
    else:
        print(f'Foram analisados {contador} números e o maior foi {maior}')
    print()
    sleep(2.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
