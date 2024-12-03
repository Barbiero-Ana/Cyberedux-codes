'''
Melhore o seu Sistema de Gestão de Orçamento
Agora ele deve:
● Usuário decide se vai inserir uma despesa ou uma receita
● Permitir inserir um número variável de receitas e despesas
● Deve mostrar na tela algum tipo de relatório ou dashboard
Desafio extra: Permita que a despesa seja adicionada em categorias como Alimentação, Transporte e 
Lazer
'''

total_transporte = 0
total_lazer = 0
total_alimentacao = 0
total_despesas = 0
total_receita = 0

while True:
    tipo = input('Digite o tipo da despesa que deseja tratar( Lazer, Alimentação, Transporte, Despesas, Receita) ou se deseja sair.')

    if tipo == 'lazer':
        total_lazer += tipo
        valor = float(input('Digite o valor da despesa: '))

