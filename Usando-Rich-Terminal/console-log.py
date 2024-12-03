import time
from rich.console import Console

console = Console()

#Acaba fornecendo o tempo que o código roda no terminal juntamente de seu nome de arquivo e diretório

for i in range(10):
    console.log(f'Doing important stuf...{i}')
    time.sleep(0.2)