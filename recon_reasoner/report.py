import os
from datetime import datetime
import json

TEMPLATE_PATH = "./templates/report_template.md"

def write(logic_flaws, metadata=None, parsed_data=None):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out_dir = "./data/outputs"
    os.makedirs(out_dir, exist_ok=True)

    if metadata is None:
        metadata = {}
    if parsed_data is None:
        parsed_data = {}

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
    report = report.replace("{{ rule_section }}", "\n".join(logic_flaws))
    report = report.replace("{{ combined_suggestions }}", "\n".join(logic_flaws))
    report = report.replace("{{ cookies }}", json.dumps(metadata.get("cookies", []), indent=2))
    report = report.replace("{{ headers }}", json.dumps(metadata.get("headers", {}), indent=2))

    # Add form details more cleanly if they are dicts
    form_section = ""
    for form in parsed_data.get("forms", []):
        form_section += f"- Action: {form.get('action')} | Method: {form.get('method')} | Inputs: {form.get('inputs')}\n"
    report = report.replace("{{ forms_section }}", form_section.strip())

    md_path = f"{out_dir}/report_{ts}.md"
    html_path = f"{out_dir}/report_{ts}.html"
    json_path = f"{out_dir}/report_{ts}.json"

    with open(md_path, "w") as f:
        f.write(report)

    with open(json_path, "w") as f:
        json.dump({
            "metadata": metadata,
            "suggestions": logic_flaws,
            "parsed": parsed_data
        }, f, indent=2)

    try:
        import markdown
        html_report = markdown.markdown(report, extensions=['fenced_code'])
        with open(html_path, "w") as f:
            f.write(html_report)
    except ImportError:
        pass
    print(f"[✓] Report generated: {md_path}")
    print(f"[✓] HTML report generated: {html_path}")
    print(f"[✓] JSON report generated: {json_path}")
    return md_path, html_path, json_path
# This function generates a report in Markdown format based on the provided logic flaws, metadata, and parsed data.
# It uses a template file to format the report and saves it in multiple formats (Markdown, HTML, JSON).
# The report includes details such as target URL, scan time, model used,
# total URLs, forms, cookies, headers, AI analysis, and rule-based suggestions.
# It also creates an output directory if it doesn't exist and handles the report generation process.
# The function returns the paths to the generated Markdown, HTML, and JSON reports.
