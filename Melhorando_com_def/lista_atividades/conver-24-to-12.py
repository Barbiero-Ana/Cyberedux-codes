'''
19. Conversor de Notação de 24h para 12h
Crie uma função converter_para_12h que receba uma hora no formato 24h e a converta
para o formato 12h com "AM" ou "PM".


'''

def converter_para_12h(hora24):
    h = int(hora24[:2])
    m = hora24[3:]
    if h == 0:
        return "12:" + m + " AM"
    if h < 12:
        return hora24 + " AM"
    if h == 12:
        return hora24 + " PM"
    return str(h - 12) + ":" + m + " PM"