import math

def adicao (a, b):
    return a + b
def subtracao (a, b):
    return a - b
def multiplicacao (a, b):
    return a * b
def divisao(a , b):
    if b!= 0:
        return a / b
    else:
        return 'Divisão por 0 não existe.'

def seno (x):
    return math.sin(math.radians(x))
def cosseno(x):
    return math.cos(math.radians(x))
def tangente(x):
    if x > 0:
        return math.tan(math.radians(x))
    else:
        return 'Erro!'
    
def log (x):
    if x > 0:
        return math.log(x)
    else:
        return 'Log de número negativo ou 0 não é possível!'
def raiz (x):
    if x > 0:
        return math.sqrt(x)
    else:
        return 'Raíz de 0 não é possível!'


