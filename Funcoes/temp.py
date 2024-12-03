def temp (y):
    return 5/9 * (y - 32)

print('conversão!')
y = float(input('Digite a temperatura em Fahrenheit: '))

print(f'Em celcius será: {temp(y) :.2f}')