print('\033[1;35m===== EX 012 =====\033[m')

def desconto():
    desc = price - price/100*5
    print(f'O valor do produto com 5% de desconto é {desc:.2f}')

    
price = float(input('Qual o preço do produto? R$'))

desconto()
