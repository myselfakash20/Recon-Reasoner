from playwright.sync_api import sync_playwright
import time
import requests

WORDLIST = ["admin", "dashboard", "login", "portal", "config", "uploads", "api", "backup"]
OPEN_REDIRECT_PATTERNS = ["redirect", "url", "next", "return"]


def crawl(target):
    metadata = {
        "target": target,
        "urls": [],
        "cookies": [],
        "headers": {},
        "forms": [],
        "params": [],
        "subdomains": [],
        "directories": [],
        "waf_detected": False,
        "waf_type": None,
        "waf_block_components": [],
        "waf_bypass_suggestions": [],
        "vuln_findings": []
    }
    page_data = ""
    with sync_playwright() as p:
        print("[~] Launching headless browser...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(target)
        time.sleep(3)
        print("[~] Extracting cookies and headers...")
        metadata["cookies"] = page.context.cookies()
        metadata["headers"] = dict(page.evaluate("() => Object.fromEntries(Object.entries(window.location))"))
        print("[~] Extracting forms and URLs...")
        metadata["forms"] = page.locator("form").all_inner_texts()
        metadata["urls"] = [link.get_attribute("href") for link in page.locator("a").all() if link.get_attribute("href")]

        print("[~] Detecting potential open redirects...")
        for url in metadata["urls"]:
            if any(p in url for p in OPEN_REDIRECT_PATTERNS):
                metadata["vuln_findings"].append(f"Possible open redirect: {url}")

        print("[~] Running directory brute-forcing...")
        for word in WORDLIST:
            try:
                resp = requests.get(f"{target.rstrip('/')}/{word}", timeout=5)
                if resp.status_code < 400:
                    metadata["directories"].append(f"{target.rstrip('/')}/{word}")
            except:
                continue

        print("[~] Pulling subdomains from crt.sh...")
        domain = target.split("//")[-1].split("/")[0]
        r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
        if r.ok:
            subdomains = set([entry["name_value"] for entry in r.json()])
            metadata["subdomains"] = list(subdomains)

        print("[~] Checking for WAF protection...")
        waf_payloads = ['<script>', '"', "'", '()', '<>', '</>']
        waf_blocked = []
        for payload in waf_payloads:
            try:
                test_url = f"{target}?test={payload}"
                res = requests.get(test_url, timeout=5)
                if res.status_code in [403, 406, 501] or 'waf' in res.text.lower():
                    waf_blocked.append(payload)
            except:
                continue

        if waf_blocked:
            metadata["waf_detected"] = True
            metadata["waf_type"] = "Generic or Cloud-based WAF"
            metadata["waf_block_components"] = waf_blocked
            metadata["waf_bypass_suggestions"] = [f"Try payload encoding or use alternate tags to bypass: {comp}" for comp in waf_blocked]

        print("[~] Running basic vulnerability checks...")
        page_text = page.content()
        if "alert(" in page_text or "<script>alert" in page_text:
            metadata["vuln_findings"].append("Possible DOM-based XSS detected")
        if "SELECT" in page_text.upper() and "FROM" in page_text.upper():
            metadata["vuln_findings"].append("Possible SQL Injection (SQL keywords found)")
        if "Content-Security-Policy" not in str(metadata["headers"]):
            metadata["vuln_findings"].append("Missing CSP Header")

        page_data = page.content()
        browser.close()
    return page_data, metadata

# This code defines a function `crawl` that uses Playwright to crawl a target URL.
# It extracts cookies, headers, forms, and links from the page.
# It also performs basic checks for WAF detection and potential vulnerabilities.
# The function returns the page content and metadata including URLs, cookies, headers, forms, and parameters.
# It uses the Playwright library to interact with the web page in a headless browser environment.
# The function also performs basic vulnerability checks and WAF detection by sending test requests with common payloads.
# If a WAF is detected, it records the type and suggests bypass methods.
# The function is designed to be used as part of a web application security analysis tool or framework
# and can be extended with more sophisticated checks and analyses as needed.
# The function is useful for security analysts and developers to quickly assess the state of a web application
# and identify potential vulnerabilities or areas that may require further investigation.
# It is designed to be easy to integrate into existing web application security analysis workflows
# and can be extended or modified to include additional checks or analyses as needed.
