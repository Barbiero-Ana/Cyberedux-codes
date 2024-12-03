'''
Escreva uma função chamada converter_segundos que recebe um número inteiro
representando segundos e retorna uma string formatada em horas, minutos e segundos (por
exemplo, converter_segundos(3661) retornaria "1 hora, 1 minuto e 1 segundo").

'''
def converter_segundos(segundos):
    horas = segundos // 3600  
    minutos = (segundos % 3600) // 60  
    segs = segundos % 60

    resultado = ''

    if horas > 0:
        resultado +=  f'{horas} hora' + ('s' if horas > 1 else '')
        if minutos > 0 or segs > 0:
            resultado += ', '
    if minutos > 0:
        resultado += f'{minutos} minuto' + ('s' if minutos > 1 else '')
        if segs > 0:
            resultado += ' e '
    if segs > 0:
        resultado += f'{segs} segundo' + ('s' if segs > 1 else '')
    return resultado
# Dentro dos () está o valor a passar pelo processo da função - LEMBRE-SE DISSO DONA ANA
def valor():
    segundos = int(input('Digite o valor a ser convertido: '))
    resultado = converter_segundos(segundos)
    print(resultado)

valor()


