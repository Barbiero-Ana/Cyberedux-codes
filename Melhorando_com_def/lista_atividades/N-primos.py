'''
8. Números Primos
Escreva uma função primo que receba um número e verifica se ele é primo ou não.


'''

def primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
