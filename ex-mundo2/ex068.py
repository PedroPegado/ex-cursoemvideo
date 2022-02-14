from random import randint
print('-=' * 21 )
print('          PAR OU ÍMPAR INSANO')
print('-=' * 21 )
v = 0
while True:
    n = int(input('Digite o seu número: '))
    comp = randint(0, 10)
    total = n + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        print('-='*21)
    print(f'Você jogou {n} e o computador {comp}, totalizando em {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[4;32mVOCÊ GANHOU!\033[m')
            v += 1
        else:
            print('\033[4;31mVOCÊ PERDEU!\033[m')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[4;32mVOCÊ GANHOU!\033[m')
            v += 1
        else:
            print('\033[4;31mVOCÊ PERDEU!\033[m')
            break
    print('-='*21)
    print('Vamos jogar novamente...')
print(f'\033[1;35mF, MAS VOCÊ GANHOU {v} VEZES.\033[m')
