'''
Desafio 1
Conversor de moedas
Crie um dicionário para armazenar taxas de câmbio (por exemplo: 'USD': 5.0, 'EUR': 6.0). Pergunte ao 
usuário um valor em Reais e uma moeda para conversão, e exiba sua taxa de conversão

'''

while True: 
    valores = {
        'USD' : 5.0,
        'EUR' : 6.0,
        'PESO ARGENTINO' : 166.46,
    }

    real = float(input('Digite o valor em real que deseja converter: '))

    for chave, valor in valores.items():
        print(f'\n{chave}: {valor}\n')

    convert = input('Digite para qual moeda você deseja converter: ').upper()


    

    if convert in valores:
        taxa = valores[convert]
        print(f'O valor {real} convertido será de: {real / taxa:.2f}')

    else:
        print('A moeda não esta na lista.')
        break




