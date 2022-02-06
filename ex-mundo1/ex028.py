print('\033[1;35m===== EX 028 =====\033[m')
import random
import time

print('-=-' * 15)
print('Vou pensar em um número de 0-5 ein...')
print('-=-' * 15)

x = int(input('Qual número tu acha que eu pensei? de 0-5 só: '))
y = random.randint(0,5)

print('Processando...')
time.sleep(3)
if x == y:
    print('ih, meteu essa? acertou mané, pensei no {} mermo.'.format(y))
else:
    print('IHHH, ERROU MANÉ USHUSHUSHAU, pensei no {} pow.'.format(y))
