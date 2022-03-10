print('='*50)
print('2 NÚMEROS INTEIROS E 1 REAL'.center(50))
print('='*50)

linha = '=' * 50

def numbers():
    int1 = int(input('\nEscreva um número inteiro: '))
    int2 = int(input('\nEscreva mais um número inteiro: '))
    float1 = float(input('\nEscreva um número real: '))
    print(f'\n{linha}')
    a = (int1 * 2) * (int2 / 2)
    b = (int1 * 3) + float1
    c = float1**3
    print(f'''\nQuestão A = {a}
Questão B = {b}
Questão C = {c}''')
    print(f'\n{linha}')

numbers()