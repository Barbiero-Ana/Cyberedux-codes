'''
23. Simulador de Caça-Níqueis
Escreva uma função caca_niquel que simule um caça-níqueis básico, retornando três
valores aleatórios e indicando um "prêmio" se os três forem iguais.

'''

def caca_niquel():
    from random import choice
    s1 = choice(["🍒", "🍋", "🍉", "⭐"])
    s2 = choice(["🍒", "🍋", "🍉", "⭐"])
    s3 = choice(["🍒", "🍋", "🍉", "⭐"])
    if s1 == s2 == s3:
        return s1 + s2 + s3 + " - Prêmio"
    return s1 + s2 + s3 + " - Tente novamente"