import random as rd
import time as tm
print('==SORTEADOR DA SORTE==')
jogos = int(input('Quantos jogos quer que seja sorteado? '))
print('Sorteando jogos...')
tm.sleep(0.7)
for j in range(0,jogos):
    sorte = [rd.randint(0, 60), rd.randint(0, 60), rd.randint(0, 60), rd.randint(0, 60),rd.randint(0, 60),
             rd.randint(0, 60)]
    print(f'Jogo {j+1} : {sorte}')
    tm.sleep(0.6)