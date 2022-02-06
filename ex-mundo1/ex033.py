print('\033[1;35m===== EX 033 =====\033[m')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite mais um número: '))

menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3
maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3

print(f'O menor numero foi: {int(menor)}')
print(f'O maior numero foi: {int(maior)}')