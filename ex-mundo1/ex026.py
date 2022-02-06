print('\033[1;35m===== EX 026 =====\033[m')

x = input('Escreva uma frase: ')

z = x.lower().strip()
y = z.count('a')
f = z.rfind('a')+1
f1 = z.find('a')+1

print(f'''A letra 'A' aparece {y} vezes''')
print(f'''Primeira letra 'A' aparece em {f1}''')
print(f'''A última letra 'A' aparece em {f}''')