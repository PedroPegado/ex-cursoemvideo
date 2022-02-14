jogador = dict()
time = list()
gol = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gol.clear()
    for c in range(0, part):
        gol.append(int(input(f'  Quantos gols na {c+1}° partida? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO!! Use apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!! Não existe jogador com o código {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  - No jogo {i+1} fez {g} gols;')
    print('-=' * 40)
print('<<< VOLTE SEMPRE >>>')
