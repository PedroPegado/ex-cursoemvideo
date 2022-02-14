import random
import time
from operator import itemgetter
jogadores = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6),
             'jogador3': random.randint(1, 6), 'jogador4': random.randint(1, 6)}
ranking = list()
print('Valores sorteados:')
time.sleep(0.7)
print(f'O jogador1 tirou {jogadores["jogador1"]}')
time.sleep(1)
print(f'O jogador2 tirou {jogadores["jogador2"]}')
time.sleep(1)
print(f'O jogador3 tirou {jogadores["jogador3"]}')
time.sleep(1)
print(f'O jogador4 tirou {jogadores["jogador4"]}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('     =- RANKING DO LEK -=')
for i, v in enumerate(ranking):
    print(f'  - {i+1}° lugar: {v[0]} com {v[1]}')
    time.sleep(0.5)