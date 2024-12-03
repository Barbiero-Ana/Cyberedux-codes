'''
18. Função para Remover Espaços
Desenvolva uma função remover_espacos que remova todos os espaços de uma string e
retorne o novo texto.

'''

def remover_espacos(texto):
    novo_texto = ""
    for i in texto:
        if i != " ":
            novo_texto += i
    return novo_texto
