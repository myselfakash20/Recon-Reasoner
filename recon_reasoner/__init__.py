
"""
Recon Reasoner
==============

An AI-powered advanced recon and vulnerability analysis tool designed for bug bounty hunters and security researchers.

Features:
- DOM-based XSS scanning
- Parameter fuzzing and heuristic analysis
- WAF detection and bypass suggestions
- Subdomain enumeration & directory brute-forcing
- Logic flaw detection using LLM
- JS parsing for endpoints, secrets, and tokens
- HTML/JSON/Markdown reporting

Author: Akash (myselfakash20)
"""

# recon_reasoner/__init__.py

import typer
import os
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

# Global config accessible across modules
CONFIG = {
    "SCAN_DEPTH": int(os.getenv("SCAN_DEPTH", 2)),
    "HEADLESS": os.getenv("HEADLESS", "true").lower() == "true",
    "WAF_PAYLOADS_PATH": os.getenv("WAF_PAYLOADS_PATH", "./data/waf_payloads.txt"),
    "USE_PROXY": os.getenv("USE_PROXY", "false").lower() == "true",
    "PROXY_URL": os.getenv("PROXY_URL", "")
}

# CLI registration for package usage
from recon_reasoner.cli import run

app = typer.Typer()
app.command()(run)

def cli():
    app()
