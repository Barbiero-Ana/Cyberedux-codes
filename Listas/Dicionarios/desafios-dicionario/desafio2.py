'''
Desafio 2
Análise de Dados Textuais
Dado um texto fornecido pelo usuário, crie um programa que:
Conte a frequência de cada palavra no texto.
Exiba as 3 palavras mais usadas.
Identifique e exiba palavras que aparecem apenas uma vez
'''

from collections import Counter

def analisar_texto(texto):
    
    palavras = texto.lower().split()

    
    frequencia = Counter(palavras)

    # Exibir a frequência de cada palavra
    print("Frequência de cada palavra:")
    for palavra, freq in frequencia.items():
        print(f"{palavra}: {freq}")

    # Exibir as 3 palavras mais usadas
    palavras_mais_usadas = frequencia.most_common(3)
    print("\nAs 3 palavras mais usadas:")
    for palavra, freq in palavras_mais_usadas:
        print(f"{palavra}: {freq}")

    # Identificar e exibir palavras que aparecem apenas uma vez
    palavras_uma_vez = [palavra for palavra, freq in frequencia.items() if freq == 1]
    print("\nPalavras que aparecem apenas uma vez:")
    if palavras_uma_vez:
        for palavra in palavras_uma_vez:
            print(palavra)
    else:
        print("Não há palavras que aparecem apenas uma vez.")


texto_usuario = input(f'\nDigite um texto: \n')


analisar_texto(texto_usuario)
