from rich.console import Console
from rich.traceback import install

install()

def add(x, y):
    a = 'Hello'
    console.log('Adding 2 numbers', log_locals=True)
    return x + y

#Forma mais eficiente para encontrar onde está o erro dentro do código.
console = Console(record=True)
try:
    add(1, 2)
    add(1, 3)
    add(1, 'a')
except:
    console.print_exception()

console.save_html