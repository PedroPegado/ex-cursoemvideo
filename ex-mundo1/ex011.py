print('\033[1;35m===== EX 011 =====\033[m')

def tinta():
    a = x*y
    t = a/2
    print(f'Sua parede tem {a}m² e a quantidade de tinta necessária será {t}L')


x = float(input('Qual a altura da sua parede? '))
y = float(input('Qual a largura da sua parede? '))

tinta()
