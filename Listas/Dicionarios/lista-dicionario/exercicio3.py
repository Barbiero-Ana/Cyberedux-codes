'''
3. Peça ao usuário para inserir seu nome, idade e cidade, e armazene as informações em um 
dicionário. Depois, exiba uma mensagem formatada com esses dados
'''

usuario = {}

while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite sua cidade: ')
    break

usuario[nome] = {
        'Nome'   : nome,
        'Idade'  : idade,
        'Cidade' : cidade,
    }

for chave, valor in usuario[nome].items():
    print(f'{chave}: {valor}')