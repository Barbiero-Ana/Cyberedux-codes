'''
22. Simulador de Jogo de Dados
Desenvolva uma função jogar_dados que simule o lançamento de dois dados e retorne a
soma. A função deve poder ser chamada várias vezes e retornar resultados aleatórios.

'''

def jogar_dados():
    from random import randint
    return randint(1, 6) + randint(1, 6)
