s = 0
for c in range(0, 6):
    x = int(input('Digite um número inteiro: '))
    if x % 2 == 0:
        s = s + x
print('{}'.format(s))
