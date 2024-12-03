'''
1 - Um clube esportivo precisa calcular a pontuação de seus atletas. Crie uma função que receba
uma lista de resultados de um atleta em 6 competições. A função deve:
- Descartar a menor e a maior pontuação
- Calcular a média das 4 pontuações restantes
- Retornar a média calculada
- Se a média for superior a 8.5, imprimir "Classificado"
- Se a média for inferior, imprimir "Não Classificado"
Exemplo de entrada: [7.5, 8.0, 9.0, 7.8, 8.5, 9.2]
'''
#[7.5, 8.0, 9.0, 7.8, 8.5, 9.2] consta como não aprovado
#[9.0, 9.5, 10.0, 8.5, 9.3, 9.7] teste

def calcular_p():

    pontuacoes =[]
    for i in range(6):
        pontuacao = float(input(f'Digite a {i+1} nota, por favor: '))
        pontuacoes.append(pontuacao)

    pontuacoes.sort()
    pontuacoes = pontuacoes[1:-1] # Remove a menor e a maior pontução dentro da lista (estudar as formas de manipular uma lista)
    media = sum(pontuacoes) / len(pontuacoes) #O len retorna a quantidade de elemtos dentro da lista 

    if media > 8.5:
        print(f'\nSua média: {media}\n')
        print(f'\nParabéns! Você foi classificado(a).\n')


    else:
        print(f'\nSua média: {media:.2f}\n')
        print('\nVocê não foi aprovado(a).\n')

calcular_p()