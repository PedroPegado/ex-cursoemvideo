def ficha(nome='<desconhecido>', gol=0):
    global nome_jogador
    global g
    if nome_jogador.isalpha() == False:
        nome = '<desconhecido>'
    if g.isdigit() == False:
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

nome_jogador = str(input('Nome jogador: ')).strip().capitalize()
g = input('Gol(s): ')
ficha(nome_jogador, g)