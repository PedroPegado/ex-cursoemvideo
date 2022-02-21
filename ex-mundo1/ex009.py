print('\033[1;35m===== EX 009 =====\033[m')

def tabuada():
    t0 = x * 0
    t1 = x * 1
    t2 = x * 2
    t3 = x * 3
    t4 = x * 4
    t5 = x * 5
    t6 = x * 6
    t7 = x * 7
    t8 = x * 8
    t9 = x * 9
    t10 = x * 10

    print('-' * 12)
    print(f'{x} x  0 = {t0}\n{x} x  1 = {t1}')
    print(f'{x} x  2 = {t2}\n{x} x  3 = {t3}')
    print(f'{x} x  4 = {t4}\n{x} x  5 = {t5}')
    print(f'{x} x  6 = {t6}\n{x} x  7 = {t7}')
    print(f'{x} x  8 = {t8}\n{x} x  9 = {t9}')
    print(f'{x} x 10 = {t10}'.format(x, t10))
    print('-' * 12)

x = int(input('Insira um número inteiro(número sem vírgula): '))

tabuada()
