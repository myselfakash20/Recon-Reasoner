import typer
from recon_reasoner import crawler, parser, analyzer, suggester, report
from rich.console import Console
from rich.panel import Panel
from pyfiglet import Figlet
import time

app = typer.Typer()
console = Console()

@app.command()
def run(target: str):
    figlet = Figlet(font='slant')
    console.print(f"[bold red]\n{figlet.renderText('Recon Reasoner')}[/bold red]")
    console.print(Panel("[bold yellow]DISCLAIMER:[/bold yellow] This tool is for authorized testing and educational purposes only. Do not scan domains you do not own or have explicit permission to test.", style="red"))
    time.sleep(1)

    console.print(f"[bold cyan]\n[+] Starting Recon Reasoner on:[/bold cyan] {target}")
    raw_data, metadata = crawler.crawl(target)
    console.print("[yellow][~] Crawling complete. Parsing data...[/yellow]")
    parsed = parser.extract(raw_data)
    console.print("[yellow][~] Parsing complete. Suggesting logic flaws...[/yellow]")
    logic_flaws = suggester.suggest(parsed)
    console.print("[yellow][~] Analyzing with AI model...[/yellow]")
    ai_insights = analyzer.analyze(parsed)

    metadata.update(ai_insights)
    report.write(logic_flaws, metadata, parsed)
    console.print("[bold green][✓] Recon complete. Reports generated.[/bold green]")

if __name__ == "__main__":
    app()


# This CLI application uses Typer to provide a command-line interface for the Recon Reasoner tool.
# It allows users to run the tool with a specified target URL, performing crawling, parsing,
# suggesting logic flaws, analyzing with AI, and generating a report.   