'''
11. Conversor de Notas de Moeda
Crie uma função converter_moeda que receba uma quantidade em reais e converta para
dólares e euros com base em taxas de câmbio fornecidas

'''

def converter_moeda(reais, taxa_dolar, taxa_euro):
    return reais * taxa_dolar, reais * taxa_euro
