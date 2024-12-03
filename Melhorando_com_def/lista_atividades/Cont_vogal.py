'''
Escreva uma função chamada contar_letras que receba uma string como parâmetro e
retorne o número de vogais e consoantes presentes na string.
'''
def cont_letras(x):
    vog = 'aeiouAEIOU'
    consot = 0
    cont_vog = 0

    for char in x:
        if char.isalpha():
            if char in vog:
                cont_vog += 1
            else:
                consot += 1
    return consot, cont_vog

string = input('Digite sua frase: ')

vog, consot = cont_letras(string)

print(f'O número de consoantes é: {consot}')
print(f' Já o valor de vogais é de: {vog}')

