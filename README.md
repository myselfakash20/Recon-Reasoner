
# 🛡️ Recon Reasoner

> AI-powered reconnaissance & logic flaw discovery tool for bug bounty hunters, red teamers, and security researchers.

---

![Recon Reasoner Banner](https://img.shields.io/badge/Recon--Reasoner-AI%20powered%20recon-blueviolet?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9%2B-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/github/license/myselfakash20/recon-reasoner?style=for-the-badge)

---

## 🚀 What is Recon Reasoner?

**Recon Reasoner** is a modular security tool that combines headless browser automation, rule-based static analysis, and LLM-driven logic flaw identification — giving you a hybrid approach to **automated recon** and **logic flaw detection**. 

Ideal for:
- 🐞 Bug bounty hunters  
- 🔐 Security researchers  
- 🕵️ Red teamers  
- 🌐 Web app pentesters  

---
![Recon Reasoner Banner](https://img.shields.io/badge/AI%20Recon-Automated-red?style=for-the-badge)


## 🔍 Features

### 🧠 AI-Powered Flaw Detection
- Uses OpenAI or LLaMA 3 (via Ollama) to suggest **logic flaws**, **trust issues**, and **authentication problems** in recon data.
- Configurable via `config.yaml`.

### 🕷️ Automated Recon with Playwright
- Headless browser-based recon to mimic real user interaction.
- Extracts:
  - DOM elements
  - Forms
  - Cookies
  - Headers
  - JS script sources
  - Hidden endpoints

### 🔎 Subdomain Enumeration
- Uses [crt.sh](https://crt.sh/) to pull public subdomains via Certificate Transparency logs.

### 🧪 Param Fuzzing (Prototype)
- Injects basic test parameters like `?admin=true`, `?redirect=https://evil.com`, etc. *(expandable!)*

### 🔒 Token & Auth Detection
- Parses HTML & JS for:
  - `csrf_token`, `auth_token`
  - Suspicious `login/auth` JS logic
  - Form methods & input names

### 📊 Multi-format Report Generation
- Markdown (`.md`)
- HTML (`.html`)
- JSON (`.json`)

| Feature | Description |
|--------|-------------|
| 🕷️ Smart Crawling | Uses Playwright to navigate and extract live data (URLs, forms, headers, cookies) |
| 🧠 AI Logic Flaw Suggestions | Uses LLMs to provide logic flaw suggestions |
| 🛡️ WAF Detection | Detects presence and type of WAFs, with blocked components and bypass tips |
| 📊 Multi-format Reporting | Generates HTML, JSON, and Markdown reports |
| 🧪 Basic Vulnerability Detection | Finds signs of XSS, SQLi, missing CSP headers, etc. |
| 🌐 Subdomain Enumeration | Queries crt.sh for discovered subdomains |
| 🧬 DOM-based XSS Scanner | JS-based payloads tested in real browser context |
| 🎯 Active Parameter Fuzzing | Payload fuzzing on GET/POST params |
| 🔐 Auth/Session Handling | Detects login forms, manages cookies/tokens, simulates login |
| 🧠 Heuristic Learning | Adapts scanning/fuzzing based on server responses |
| 📜 JavaScript Parsing | Parses inline/external JS for keys, URLs, secrets |
| 📡 WAF Fingerprinting | Detects WAF vendor like Cloudflare, AWS WAF, etc. |
| 🔁 Open Redirect Detection | Detects possible redirect-based vulnerabilities |
| 📂 Directory Discovery | Looks for accessible hidden paths and tests fuzzing |

---

## ⚙️ Setup Instructions

### 1. 📦 Install Dependencies

```bash
git clone https://github.com/myselfakash20/recon-reasoner.git
cd recon-reasoner
pip install -r requirements.txt
playwright install
```

---

### 2. 🤖 Setup LLM Engine

#### Option A: Use Ollama (local LLaMA 3)
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3
```

Update `config.yaml`:
```yaml
llm:
  mode: "local"
  model: "llama3"
```

#### Option B: Use OpenAI GPT
Update `config.yaml`:
```yaml
llm:
  mode: "openai"
  model: "gpt-4"
  openai_key: "your-openai-key"
```

---

### 3. 🚀 Run the Tool

```bash
ollama run llama3

```
```bash
playwright run-server
```
```bash
python3 main.py run https://example.com
```

You'll see output like:

```bash
[+] Starting Recon Reasoner on: https://example.com
[~] Crawling complete. Parsing data...
[~] Suggesting logic flaws...
[~] Analyzing with AI model...
[✓] Recon complete. Reports generated in /data/outputs/
```
---

## 📁 Output

Reports are saved in `data/outputs/` with three formats:
- `report_*.md`: Full markdown report
- `report_*.html`: Styled HTML version
- `report_*.json`: Machine-readable JSON for automation

## 📜 Sample Report Sections

- **AI-based logic flaw insight**
- **Forms and input analysis**
- **WAF detection report with bypass tips**
- **JS/DOM interaction result**
- **Heuristic and fuzzing-based vulnerabilities**

## 📎 Example Logic Flaw Insight
```
Untrusted input in search field, no CSRF tokens found, tokenless POST endpoint, etc.
```

---

## 💡 Use Cases for Security Research

| Module         | What It Helps You Discover                                         |
|----------------|---------------------------------------------------------------------|
| `crawler.py`   | Hidden forms, exposed JS, link enumeration, cookies & headers       |
| `parser.py`    | Token leaks, insecure form methods, auth-related JS functions       |
| `suggester.py` | Missing CSRFs, client-side validation issues, logic flaws           |
| `analyzer.py`  | Custom reasoning on logic errors using OpenAI / LLaMA               |
| `report.py`    | Markdown/HTML reports for triage & writeups                         |

---

## 🧩 Roadmap

- [ ] Auth bypass tester
- [ ] Param brute module
- [ ] JS endpoint crawler
- [ ] Plugin support
- [ ] HTML UI for recon

---

## ⚠️ Disclaimer

> This tool is intended for educational and ethical hacking and authorized testing only. 
> Do **not** use it against systems without explicit permission.


---

## 🙌 Credits

- Built with ❤️ by [Akash](https://github.com/myselfakash20)
- Inspired by bug bounty, logic flaws & AI-assisted recon

---
## 🪪 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Contribution

PRs welcome! Let's build a smarter recon assistant for bug bounty hunters and red teamers.

---

## 📫 Contact

Need help or want to collaborate?  
📧 Twitter: [@myselfakash20](https://twitter.com/myselfakash20)  
📂 GitHub: [github.com/myselfakash20](https://github.com/myselfakash20)

---

**Happy Hacking!** 🧠💥
