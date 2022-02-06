print('\033[1;35m===== EX 008 =====\033[m')

m = float(input('Número em metros: '))

km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print(f'Em quilômetro: {km}')
print(f'Em hectômetro: {hm}')
print(f'Em decâmetro: {dam}')
print(f'Em decímetro: {dm}')
print(f'Em centímetro: {cm}')
print(f'Em milímetro: {mm}')