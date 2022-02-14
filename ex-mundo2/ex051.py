print('pa pa pa')
comeco = int(input('Digite o número inicial: '))
razao = int(input('De quanto em quanto: '))
fim = int(input('Até qual número: '))
for pa in range(comeco, fim, razao):
    print(pa)
if fim < comeco:
    print('INVÁLIDO. TENTE NOVAMENTE.')