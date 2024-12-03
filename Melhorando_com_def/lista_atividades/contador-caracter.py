'''
9. Contador de Caracteres em um Texto
Crie uma função contar_caracteres que recebe uma string e um caractere específico. A
função deve retornar o número de vezes que o caractere aparece na string.

'''

def contar_caracteres(texto, caractere):
    c = 0
    for i in texto:
        if i == caractere:
            c += 1
    return c
