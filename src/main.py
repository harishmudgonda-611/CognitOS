from rich.console import Console
from datetime import datetime
import platform


console = Console()

console.print("[bold green]🚀 CognitOS v0.1[/bold green]")
console.print(f"Time: {datetime.now()}")
console.print(f"Python: {platform.python_version()}")
console.print("[cyan]System Ready[/cyan]\n")

while True:
    prompt = console.input("[bold blue]You:[/bold blue] ")

    if prompt.lower() in ["exit", "quit"]:
        break

    try:
        reply = chat(prompt)
        console.print(f"\n[bold green]CognitOS:[/bold green] {reply}\n")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
