### Ollama Setup for Recon Reasoner

1. Install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. Download the LLaMA3 model:
```bash 
ollama run llama3
```

3. Leave it running in the background (it serves at localhost)

4. Run Recon Reasoner:
```bash
python main.py https://example.com
```
