x = int(input('Até qual termo vc quer? '))
t1 = 0
t2 = 1

print(f'{t1} -> {t2}',end=' ')
cont = 3
while cont <= x:
    t3 = t1 + t2
    print(f'-> {t3}',end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')

