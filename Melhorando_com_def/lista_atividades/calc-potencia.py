'''
17. Calcular Potência
Crie uma função potencia que receba dois parâmetros, base e expoente, e calcule a
potência usando apenas multiplicação repetida (sem o operador **).
'''

def potencia(base, expoente):
    p = 1
    i = 0
    while i < expoente:
        p *= base
        i += 1
    return p
