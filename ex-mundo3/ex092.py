import datetime
import time

pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.datetime.now().year - ano
pessoa['Carteira'] = int(input('Você tem carteira de trabalho? (se não, digite 0): '))
if pessoa['Carteira'] != 0:
    pessoa['Contratação'] = int(input('Qual o ano da sua contratação? '))
    pessoa['Salário'] = float(input('Qual o seu salário? R$'))
    pessoa['Aposentadoria'] = (datetime.datetime.now().year - ano) + 35
for k, v in pessoa.items():
    print(f'O campo {k} tem valor {v}.')



