'''
Crie uma função calcular_juros_compostos que receba como parâmetros o capital inicial,
a taxa de juros e o número de períodos, e retorne o valor final acumulado. A função deve
utilizar a fórmula de juros compostos: A = P (1 + r)^n, onde A é o montante final, P é o capital
inicial, r é a taxa de juros, e n o número de períodos.
'''

def juros_compost():
    capital = float(input('Digite o valor do capital inicial: '))
    taxa_jur = float(input('Digite o valor do juros: '))
    period = float(input('Digite o número de períodos: '))

    if taxa_jur > 1 :
        taxa_jur =  taxa_jur / 100
    
    montante = capital * (1 + taxa_jur) ** period
    print(f'O montante após {period} períodos será: {montante:.2f}')

juros_compost()
