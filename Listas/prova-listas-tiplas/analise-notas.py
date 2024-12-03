'''
5 - Desenvolva um sistema de análise de desempenho acadêmico que:
- Receba uma lista de notas de um aluno
- Calcule a média final
- Identifique o número de notas abaixo de 7.0
- Determine o conceito final:
A: média >= 9.0
B: 8.0 <= média < 9.0
C: 7.0 <= média < 8.0
D: média < 7.0
- Imprima um relatório detalhado
Exemplo de entrada: [8.5, 7.2, 9.0, 6.5, 8.0]
'''

def analise_not():

    notas = []
    quantd = int(input('Digite quantas notas deseja inserir: '))

    for i in range (quantd):
        nota = float(input(f'Digite o valor da  {i + 1 } nota: '))
        notas.append(nota)
    
    media = sum(notas) / len(notas)

    menor_sete = [nota for nota in notas if nota < 7.0]

    if media >= 9.0:
        conceito = 'A'

    elif 8.0 <= media <= 9.0:
        conceito = 'B'
    
    elif 7.0 <= media <= 8.0:
        conceito = 'C'
    
    else:
        conceito = 'D'

    print('\n======================================================================================================================\n')
    print(f'\n Média final: {media:.2f}')
    print(f'\nNotas abaixo de 7: {menor_sete}')
    print(f'\nConceito final: {conceito}')

analise_not()