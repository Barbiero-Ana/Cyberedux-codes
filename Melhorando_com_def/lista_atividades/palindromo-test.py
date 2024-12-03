'''
13. Teste de Palíndromo
Crie uma função eh_palindromo que receba uma string e verifique se ela é um palíndromo,
ou seja, se pode ser lida da mesma forma de trás para frente.

'''


def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    i = 0
    j = len(texto) - 1
    while i < j:
        if texto[i] != texto[j]:
            return False
        i += 1
        j -= 1
    return True
