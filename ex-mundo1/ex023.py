print('\033[1;35m===== EX 023 =====\033[m')

x = int(input('Digite um número de 0-9999: '))

u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')