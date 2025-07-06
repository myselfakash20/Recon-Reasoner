from bs4 import BeautifulSoup
import re

def extract(page_data):
    soup = BeautifulSoup(page_data, "html.parser")
    endpoints = [tag["src"] for tag in soup.find_all("script", src=True)]
    endpoints += [tag["href"] for tag in soup.find_all("a", href=True)]
    endpoints += [form.get("action") for form in soup.find_all("form") if form.get("action")]
    endpoints = list(set(filter(lambda x: x and x.startswith("http"), endpoints)))

    forms = []
    for form in soup.find_all("form"):
        form_info = {
            "action": form.get("action"),
            "method": form.get("method", "get").lower(),
            "inputs": [input.get("name") for input in form.find_all("input") if input.get("name")]
        }
        forms.append(form_info)

    tokens = re.findall(r'(csrf[_-]token|auth[_-]?token)["\']?\s*[:=]\s*["\']([a-zA-Z0-9-_]+)', page_data, re.IGNORECASE)
    token_list = [t[1] for t in tokens]

    scripts = [script.string for script in soup.find_all("script") if script.string]
    js_keywords = [kw for js in scripts for kw in re.findall(r'login|auth|token|csrf', js, re.IGNORECASE)]

    return {
        "endpoints": endpoints,
        "tokens": token_list,
        "forms": forms,
        "js_keywords": list(set(js_keywords))
    }

# This function extracts endpoints, forms, security tokens, and JavaScript keywords from the provided HTML page data.
# It uses BeautifulSoup to parse the HTML and regex to find specific patterns.
# The extracted data is returned in a structured dictionary format.
# The endpoints include script sources, links, and form actions.
# The forms include action URLs, methods, and input names.
# Security tokens are identified by common patterns like "csrf_token" or "auth_token".