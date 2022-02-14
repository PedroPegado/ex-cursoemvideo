def fatorial(n, show=False):
    """
    -> CALCULA O FATORIAL DE UM NÚMERO.
    :param n: Número que irá ser calculado.
    :param show: Mostrar ou não a conta (opcional)
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1 ):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-=' * 15)
print('  CALCULO DE FATORIAL')
print('-=' * 15)
num = int(input('Digite o seu número: '))
print('-' * 20)
print('Se quiser ver a conta digite T, se não, digite F.')
tf = str(input('True ou False[T/F]: ')).strip().upper()[0]
if tf == 'T':
    j = 'show=True'
elif tf == 'F':
    j = ''
print('-' * 20)
print(fatorial(num, j))