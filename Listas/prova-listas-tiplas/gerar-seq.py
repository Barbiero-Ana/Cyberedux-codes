'''
4 - Implemente uma função gerar_sequencia_personalizada(inicio, fim, regra)
que:
- Receba um intervalo de início e fim
- Aplique uma regra de transformação personalizada
- Retorne uma nova lista com os números transformados
- Algumas regras possíveis:
- Dobrar o valor
- Elevar ao quadrado
- Somar 10
- Subtrair 5
Exemplo de entrada: inicio=1, fim=5, regra="dobrar
'''

def gerar_seq():

    inicio = int(input('Digite o inicio do intervalo: '))
    fim = int(input('Digite o fim do intervalo: '))
    print('\nDigite qual regra você deseja aplicar ao intervalo.\n')
    regra = int(input('1 - Dobrar\n2 - Elevar ao quadrado\n3 - Somar mais 10\n4 - Subtrair 5\n: '))

    if regra == 1:
        sequencia = [ x * 2 for x in range(inicio, fim + 1)]

    elif regra == 2:
        sequencia = [ x ** 2 for x in range(inicio, fim + 1)]

    elif regra == 3:
        sequencia = [ x + 10 for x in range (inicio, fim + 1)]
    
    elif regra == 4:
        sequencia = [ x - 5 for x in range(inicio, fim + 1)]

    else: 
        sequencia = []

    print(f'\nA sequência gerada foi: {sequencia}\n')

gerar_seq()