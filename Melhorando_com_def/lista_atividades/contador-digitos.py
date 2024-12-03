'''
12. Contador de Dígitos em um Número
Crie uma função contar_digitos que receba um número e retorne a quantidade de dígitos
nele presente. Exemplo: contar_digitos(12345) retorna 5.


'''

def contar_digitos(numero):
    c = 0
    while numero > 0:
        numero //= 10
        c += 1
    return c
