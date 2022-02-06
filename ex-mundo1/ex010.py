print('\033[1;35m===== EX 010 =====\033[m')

real = float(input('Quanto você tem na carteira? R$'))
dol = real/5.33

print(f'Com esse valor de R${real}(REAL), você pode adquirir USD{dol:.3}(DÓLAR)')