jogador = dict()
v = list()

jogador['nome'] = str(input('Qual o nome do jogador? '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, part):
    v.append(int(input(f'  Quantos gols na {c+1}° partida? ')))
jogador['gols'] = v[:]
jogador['total'] = sum(v)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  =>Na {i+1}° partida, o jogador marcou {v} gols.')
print(f'Ao total foram {jogador["total"]} gols.')