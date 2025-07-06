from playwright.sync_api import sync_playwright
import time
import requests

def crawl(target):
    metadata = {"target": target, "urls": [], "cookies": [], "headers": {}, "forms": [], "params": [], "subdomains": []}
    page_data = ""
    with sync_playwright() as p:
        print("[~] Launching headless browser...")
        browser = p.chromium.launch(headless=False)  # Set to False for debugging
        print("[~] Opening new page...")
        print(f"[~] Navigating to target: {target}")
        page = browser.new_page()
        page.goto(target)
        time.sleep(3)
        print("[~] Extracting cookies and headers...")
        metadata["cookies"] = page.context.cookies()
        metadata["headers"] = dict(page.evaluate("() => Object.fromEntries(Object.entries(window.location))"))
        print("[~] Extracting forms and URLs...")
        metadata["forms"] = page.locator("form").all_inner_texts()
        metadata["urls"] = [link.get_attribute("href") for link in page.locator("a").all() if link.get_attribute("href")]
        print("[~] Running parameter brute-forcing & auth check...")
        metadata["params"] = ["id=1", "admin=true", "redirect=https://evil.com"]  # example static param fuzzing list
        print("[~] Pulling subdomains from crt.sh...")
        domain = target.split("//")[-1].split("/")[0]
        r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json")
        if r.ok:
            subdomains = set([entry["name_value"] for entry in r.json()])
            metadata["subdomains"] = list(subdomains)
        page_data = page.content()
        browser.close()
    return page_data, metadata


# This function crawls the target URL using Playwright, extracting cookies, headers, forms, and links.
# It returns the page content and metadata including URLs, cookies, headers, and forms.
# The Playwright library is used to interact with the web page in a headless browser environment    