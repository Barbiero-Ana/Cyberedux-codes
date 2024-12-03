'''
7. Soma dos Quadrados
Crie uma função soma_dos_quadrados que recebe um número inteiro positivo n e retorne a
soma dos quadrados de todos os números de 1 até n. Exemplo: para n = 3, o resultado será
1^2 + 2^2 + 3^2 = 14
'''

def soma_dos_quadrados(n):
    i = 1
    s = 0
    while i <= n:
        s += i * i
        i += 1
    return s