print('======TABUADA BRABA======')
tabuada = n1 = 0
while True:
    n1 = int(input('Digite o numero: '))
    if n1 < 0:
        break
    print('-' * 25)
    for tabuada in range (1, 11):
        print('{} x {} = {}'.format(n1, tabuada, n1*tabuada))
    print('-' * 25)
    tabuada += 1
    if n1 < 0:
        break
print('TABUADA ENCERRADA.')



