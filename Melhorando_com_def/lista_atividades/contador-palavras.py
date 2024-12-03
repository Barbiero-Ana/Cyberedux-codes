'''
6. Contador de Palavras em uma Frase
Crie uma função chamada contar_palavras que receba uma string como entrada e retorne
a quantidade de palavras na frase. Considere que as palavras são separadas por espaços.

'''

def contar_palavras(frase):
    palavras = 0
    for i in frase:
        if i == " ":
            palavras += 1
    return palavras + 1
