import random
import time

print('\033[1;36;40m-=\033[m'*12)
print('\033[1;36;45m        JOKENPÔ         \033[m')
print('\033[1;36;40m-=\033[m'*12)

x = str(input('\n\033[1;35mVAMOS JOGAR JOKENPÔ, PEDRA PAPEL OU TESOURA?\033[m ')).strip().lower()
joken = ['pedra', 'papel', 'tesoura']
y = random.choice(joken)

print('JO ',end='')
time.sleep(0.7)
print('KEN ',end='')
time.sleep(0.7)
print('PO!!',end=' ')
time.sleep(0.7)
print('\033[1;36m{}\033[m'.format(y.title()))
time.sleep(0.5)

if x == 'pedra' and y == 'tesoura' \
        or x == 'papel' and y == 'pedra'\
        or x == 'tesoura' and y == 'papel':
    print('\033[1;32mVOCÊ GANHOU, VOCÊ REALMENTE É UM ADVERSÁRIO A ALTURA.\033[m')
elif y == 'pedra' and x == 'tesoura' \
        or y == 'papel' and x == 'pedra'\
        or y == 'tesoura' and x == 'papel':
    print('\033[1;31mVOCÊ PERDEU, NEWBA.\033[m')
elif y == 'pedra' and x == 'pedra' \
        or y == 'tesoura' and x == 'tesoura' \
        or y == 'papel' and x == 'papel':
    print('\033[1;33mEMPATAMOS, VAMOS MAIS UMA VEZ.\033[m')

