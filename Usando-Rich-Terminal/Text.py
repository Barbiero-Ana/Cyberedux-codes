from rich.console import Console
from rich.text import Text

console = Console()

console.print('A bit of text.', style='bold underline green')
console.print('[bold] A bit of [cyan]text with[/] some color[/]')

text = Text('Hello world!')
text.stylize('bold magenta', 0 ,6)
console.print(text)