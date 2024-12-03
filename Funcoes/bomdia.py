def hor_dia(x,):
    
    if x >= 5 and x <= 11:
        return 'Bom dia!'
    elif x >= 12 and x <=17:
        return 'Boa tarde!'
    else:
        return 'Boa noite!'

x = int(input('Digite a hora atual: '))

print(f'Hora atual: {x}:00, portanto... {hor_dia(x)}')