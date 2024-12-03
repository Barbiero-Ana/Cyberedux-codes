'''
15. Função para Maior de Três Números
Crie uma função maior_de_tres que receba três números como parâmetros e retorne o
maior deles.

'''

def maior_de_tres(a, b, c):
    if a > b and a > c:
        return a
    if b > c:
        return b
    return c
