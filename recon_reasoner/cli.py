import typer
import pyfiglet
from rich import print
from rich.panel import Panel
from recon_reasoner import crawler, parser, analyzer, suggester, report

app = typer.Typer()

@app.command()
def run(target: str):
    banner = pyfiglet.figlet_format("Recon Reasoner")
    print(f"[bold cyan]{banner}[/bold cyan]")
    print(Panel.fit("[bold yellow]AI-powered recon & logic flaw detector\nUse responsibly. For legal testing only.[/bold yellow]", title="[bold red]Disclaimer[/bold red]"))

    print(f"[green][+] Starting Recon Reasoner on:[/green] {target}")
    raw_data, metadata = crawler.crawl(target)
    print("[blue][~] Crawling complete. Parsing data...[/blue]")
    parsed = parser.extract(raw_data)
    print("[blue][~] Parsing complete. Suggesting logic flaws...[/blue]")
    logic_flaws = suggester.suggest(parsed)
    print("[blue][~] Analyzing with AI model...[/blue]")
    ai_insights = analyzer.analyze(parsed)

    metadata.update(ai_insights)
    report.write(logic_flaws, metadata, parsed)
    print("[bold green][✓] Recon complete. Reports generated.[/bold green]")

if __name__ == "__main__":
    app()



# This CLI application uses Typer to provide a command-line interface for the Recon Reasoner tool.
# It allows users to run the tool with a specified target URL, performing crawling, parsing,
# suggesting logic flaws, analyzing with AI, and generating a report.   
