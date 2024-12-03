from rich.console import Console
from rich.theme import Theme

#criando keys de personalização personalizados (como se fossem apelidos para cada parametro)
custom_theme = Theme({'success': 'green', 'error': 'bold red'})

console = Console(theme=custom_theme)

console.print('Operation Successful', style='success')
console.print('Operation failed!', style='error')
console.print('Operation [error] failed![/error]')