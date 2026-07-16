from rich.console import Console
from datetime import datetime
import platform

console = Console()

console.print("[bold green]🚀 Cognit OS v0.1[/bold green]")
console.print(f"Time: {datetime.now()}")
console.print(f"Python: {platform.python_version()}")
console.print("[cyan]System Ready[/cyan]")

