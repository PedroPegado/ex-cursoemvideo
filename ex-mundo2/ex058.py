from random import randint
computador = randint(0,10)
print('Pensei em um número de 0 a 10, consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ein...')
        elif jogador > computador:
            print('Menos ein...')
print(f'Acertou com {palpites} tentativas.')
