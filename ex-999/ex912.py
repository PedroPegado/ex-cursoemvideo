linha = '\033[1;96m=\033[m' * 50
print(linha)
print('VELOCIDADE INTERNET'.center(50))
print(linha)
min = 0

def internet():
    download = float(input('Digite o tamanho do arquivo que você irá baixar(em MB): '))
    velo_net = float(input('Digite a velocidade de download da sua internet(em Mbps): '))
    tempo = (download/(velo_net / 8))
    print(f'{linha}')
    if tempo < 60:
        print(f'\nO tempo estimado para download é de {tempo:.2f} segundos.')
    else:
        print(f'\nO tempo estimado para download é de {tempo/60:.2f} Minutos.')
    print(f'\n{linha}')

internet()