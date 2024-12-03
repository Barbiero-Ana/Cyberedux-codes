'''
5. Conversor de Datas
Escreva uma função converter_data que recebe uma data no formato DD/MM/AAAA e
converte para um formato escrito, como "23 de Novembro de 2024".


'''


def converter_data(data):
    m = int(data[3:5])
    if m == 1:
        mes = "Janeiro"
    elif m == 2:
        mes = "Fevereiro"
    elif m == 3:
        mes = "Março"
    elif m == 4:
        mes = "Abril"
    elif m == 5:
        mes = "Maio"
    elif m == 6:
        mes = "Junho"
    elif m == 7:
        mes = "Julho"
    elif m == 8:
        mes = "Agosto"
    elif m == 9:
        mes = "Setembro"
    elif m == 10:
        mes = "Outubro"
    elif m == 11:
        mes = "Novembro"
    elif m == 12:
        mes = "Dezembro"
    return data[:2] + " de " + mes + " de " + data[6:]
