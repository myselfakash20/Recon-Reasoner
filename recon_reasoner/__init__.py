
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

from . import cli
from . import crawler
from . import parser
from . import analyzer
from . import suggester
from . import report
from . import utils
from . import scanners

__all__ = [
    "cli",
    "crawler",
    "parser",
    "analyzer",
    "suggester",
    "report",
    "utils",
    "scanners"
]
