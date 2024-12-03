'''

21. Simulador de Pedra, Papel e Tesoura
Desenvolva uma função pedra_papel_tesoura que receba a jogada de dois jogadores e
retorne o vencedor.

'''

def pedra_papel_tesoura(j1, j2):
    if j1 == j2:
        return "Empate"
    if (j1 == "pedra" and j2 == "tesoura") or (j1 == "tesoura" and j2 == "papel") or (j1 == "papel" and j2 == "pedra"):
        return "Jogador 1"
    return "Jogador 2"