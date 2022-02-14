#while True:
#    print('-' * 20)
#    n = str(input('Digite um número: '))
#    if n.isnumeric():
#        print('-' * 20)
#        print(f'Você acabou de digitar o número {n}.')
#        break
#    else:
#        print('\033[4;31mERRO, TENTE NOVAMENTE.\033[m')
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[4;31mERRO, TENTE NOVAMENTE.\033[m')
        if ok:
            break
    return valor


n = str(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}.')

