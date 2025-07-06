import requests
import yaml

def analyze(data):
    config = yaml.safe_load(open("config.yaml"))
    if config["llm"]["mode"] == "none":
        return {"ai_analysis": "LLM disabled.", "model": "none"}

    if config["llm"]["mode"] == "openai":
        import openai
        openai.api_key = config["llm"]["openai_key"]
        response = openai.ChatCompletion.create(
            model=config["llm"]["model"],
            messages=[
                {"role": "system", "content": "You are a web security analyst."},
                {"role": "user", "content": f"Analyze this:\n{data}"}
            ]
        )
        return {"ai_analysis": response["choices"][0]["message"]["content"], "model": config["llm"]["model"]}

    # Default to local
    prompt = f"Analyze the following web app structure for logic flaws:\n{data}"
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": config["llm"]["model"],
        "prompt": prompt,
        "stream": False
    })
    suggestion = res.json().get("response", "")
    return {"ai_analysis": suggestion, "model": config["llm"]["model"]}

# This function analyzes the provided data using a configured LLM.
# It supports both OpenAI and local LLaMA models based on the configuration.
# It returns the AI analysis and the model used for the analysis.   
