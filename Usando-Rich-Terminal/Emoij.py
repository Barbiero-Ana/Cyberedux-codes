from rich.console import Console
from rich.theme import Theme

#criando keys de personalização personalizados (como se fossem apelidos para cada parametro)
custom_theme = Theme({'success': 'green', 'error': 'bold red'})

console = Console(theme=custom_theme)

console.print('Operation Successful', style='success')
console.print('Operation failed!', style='error')
console.print('Operation [error] failed![/error]')

# EMOJI #
#''Thumbs_up - nome do emoji de joinha
#Para adicionar o emoji basta digitar seu nome entre dois pontos (::)

console.print(':thumbs_up: file dowloaded!')
console.print(':apple: :bug:')