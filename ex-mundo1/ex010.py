print('\033[1;35m===== EX 010 =====\033[m')

def dolar():
    dol = real/5.09
    print(f'Com esse valor de R${real}(REAL), você pode adquirir USD{dol:.3}(DÓLAR)')

real = float(input('Quanto você tem na carteira? R$'))

dolar()
