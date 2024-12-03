'''
23.2.0 Simulador de Caça-Níqueis
Escreva uma função caca_niquel que simule um caça-níqueis básico, retornando três
valores aleatórios e indicando um "prêmio" se os três forem iguais.

'''

def caca_niquel():
    from random import randint
    s1 = randint(1, 5)
    s2 = randint(1, 5)
    s3 = randint(1, 5)
    if s1 == s2 == s3:
        return str(s1) + str(s2) + str(s3) + " - Prêmio"
    return str(s1) + str(s2) + str(s3) + " - Tente novamente"
