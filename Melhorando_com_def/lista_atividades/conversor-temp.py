'''
10. Conversão de Unidades de Temperatura
Desenvolva uma função converter_temperatura que receba uma temperatura em Celsius
e a converta para Fahrenheit e Kelvin.

'''
def converter_temperatura(c):
    f = c * 9 / 5 + 32
    k = c + 273.15
    return f, k
