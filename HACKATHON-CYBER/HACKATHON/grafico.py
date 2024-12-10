import plotext as plt

# Dados
a = ['jan', 'fev', 'mar', 'abr']  # Rótulos para o eixo X
b = [100, 3000, 450, 300]         # Valores para o eixo Y

# Usando índices numéricos no eixo X
x = list(range(1, len(a) + 1))  # [1, 2, 3, 4]

# Criando o gráfico
plt.plot(x, b)  # Plota os valores
plt.title("Vendas Mensais")  # Título do gráfico
plt.xlabel("Meses")          # Nome do eixo X
plt.ylabel("Valores")        # Nome do eixo Y
plt.xticks(x, a)             # Define os rótulos do eixo X
plt.show()                   # Exibe o gráfico
