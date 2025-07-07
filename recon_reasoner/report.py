import os
from datetime import datetime
import json

TEMPLATE_PATH = "./templates/report_template.md"

def write(data, metadata=None, parsed_data=None):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_dir = "./data/outputs"
    os.makedirs(out_dir, exist_ok=True)

    if metadata is None:
        metadata = {}

    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    report = template
    report = report.replace("{{ target }}", metadata.get("target", "N/A"))
    report = report.replace("{{ scan_time }}", ts)
    report = report.replace("{{ model }}", metadata.get("model", "N/A"))
    report = report.replace("{{ depth }}", str(metadata.get("depth", 0)))
    report = report.replace("{{ total_urls }}", str(len(metadata.get("urls", []))))
    report = report.replace("{{ total_forms }}", str(len(metadata.get("forms", []))))
    report = report.replace("{{ total_cookies }}", str(len(metadata.get("cookies", []))))
    report = report.replace("{{ total_headers }}", str(len(metadata.get("headers", {}))))
    report = report.replace("{{ ai_section }}", metadata.get("ai_analysis", "None"))
    report = report.replace("{{ rule_section }}", "\n".join(data))
    report = report.replace("{{ combined_suggestions }}", "\n".join(data))
    report = report.replace("{{ cookies }}", json.dumps(metadata.get("cookies", []), indent=2))
    report = report.replace("{{ headers }}", json.dumps(metadata.get("headers", {}), indent=2))
    report = report.replace("{{ forms_section }}", "\n".join(metadata.get("forms", [])))

    waf_info = f"Detected: {metadata.get('waf_detected')}\n"
    waf_info += f"Type: {metadata.get('waf_type')}\n"
    waf_info += f"Blocked Components: {metadata.get('waf_block_components')}\n"
    waf_info += f"Bypass Suggestions: {metadata.get('waf_bypass_suggestions')}\n"
    report += f"\n## 🔥 WAF Detection\n{waf_info}"

    if metadata.get("vuln_findings"):
        report += f"\n## 🚨 Vulnerability Findings\n" + "\n".join(f"- {v}" for v in metadata["vuln_findings"])

    md_path = f"{out_dir}/report_{ts}.md"
    html_path = f"{out_dir}/report_{ts}.html"
    json_path = f"{out_dir}/report_{ts}.json"

    with open(md_path, "w") as f:
        f.write(report)

    with open(json_path, "w") as f:
        json.dump({
            "metadata": metadata,
            "suggestions": data,
            "parsed": parsed_data
        }, f, indent=2)

    try:
        import markdown
        html_report = markdown.markdown(report, extensions=['fenced_code'])
        with open(html_path, "w") as f:
            f.write(html_report)
    except ImportError:
        pass
#         resp = requests.get(test_url, timeout=5)
#         if resp.status_code == 403:
#             metadata["waf_detected"] = True
#             metadata["waf_type"] = "Generic WAF"
# from recon_reasoner.crawler import crawl
#         metadata["vuln_findings"].append("Basic vulnerability checks not implemented yet.")
#         metadata["vuln_findings"].append("Basic vulnerability checks not implemented yet.")

# This function generates a report in Markdown format based on the provided logic flaws, metadata, and parsed data.
# It uses a template file to format the report and saves it in multiple formats (Markdown, HTML, JSON).
# The report includes details such as target URL, scan time, model used,
# total URLs, forms, cookies, headers, AI analysis, and rule-based suggestions.
# It also creates an output directory if it doesn't exist and handles the report generation process.
# The function returns the paths to the generated Markdown, HTML, and JSON reports.
