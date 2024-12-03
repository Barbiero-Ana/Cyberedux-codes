'''
4. Conversão de Notas
Desenvolva uma função converter_notas que recebe uma lista de notas de alunos em
formato de letra (A, B, C, D, F) e as converta para notas numéricas de acordo com uma tabela
de conversão fornecida
'''

def converter_notas(nota):
    if nota == "A":
        return 10
    elif nota == "B":
        return 8
    elif nota == "C":
        return 6
    elif nota == "D":
        return 4
    elif nota == "F":
        return 0
