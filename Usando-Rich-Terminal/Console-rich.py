from rich.console import Console

console = Console()

console.print('Some text')
console.print('Text with style', style= 'bold')
console.print('Text with more style', style= 'bold underline')
console.print('Text with more style and color', style= 'bold underline green')
console.print('Text with more style and 2 colors', style= 'bold underline red on white') #Primeira cor é a cor da letra e a segunda cor a cor do fundo no qual a frase fica

console.print('[bold]Text with [cyan]some parts[/] with style[/]')