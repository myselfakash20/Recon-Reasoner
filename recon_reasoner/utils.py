# recon_reasoner/utils.py

from urllib.parse import urlparse
import re
import json
import yaml
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def normalize_url(url):
    if not url.startswith("http"):
        return f"http://{url}"
    return url

def format_report_data(data):
    formatted = []
    for key, value in data.items():
        if isinstance(value, list):
            formatted.append(f"{key}: {', '.join(value)}")
        elif isinstance(value, dict):
            formatted.append(f"{key}: {', '.join(f'{k}={v}' for k, v in value.items())}")
        else:
            formatted.append(f"{key}: {value}")
    return "\n".join(formatted)

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc if parsed_url.netloc else parsed_url.path.split('/')[0]

def is_valid_url(url):
    return bool(re.match(r'^(https?://)?([a-zA-Z0-9.-]+)(:\d+)?(/.*)?$', url))

def is_valid_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def is_valid_ip(ip):
    return bool(re.match(r'^((25[0-5]|(2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|(2[0-4][0-9]|[01]?[0-9][0-9]?))$', ip))

def is_valid_ipv6(ipv6):
    return bool(re.match(r'^([0-9a-fA-F]{1,4}:){1,7}[0-9a-fA-F]{1,4}$', ipv6))

def is_valid_base64(s):
    return bool(re.match(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$', s))

def is_valid_uuid(s):
    return bool(re.match(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', s))

def is_valid_date(s):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', s))

def is_valid_time(s):
    return bool(re.match(r'^\d{2}:\d{2}:\d{2}$', s))

def is_valid_datetime(s):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$', s))

def is_valid_color(s):
    return bool(re.match(r'^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$', s))

def is_valid_phone(s):
    return bool(re.match(r'^\+?[1-9]\d{1,14}$', s))

def is_valid_credit_card(s):
    return bool(re.match(r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9]{2})[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$', s))

def is_valid_password(s):
    return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', s))

def is_valid_username(s):
    return bool(re.match(r'^[a-zA-Z0-9._-]{3,}$', s))

def is_valid_query_string(s):
    return bool(re.match(r'^[a-zA-Z0-9_]+=[a-zA-Z0-9_]+(&[a-zA-Z0-9_]+=[a-zA-Z0-9_]+)*$', s))

def is_valid_path(s):
    return bool(re.match(r'^(\/[a-zA-Z0-9._-]+)+$', s))

def is_valid_filename(s):
    return bool(re.match(r'^[a-zA-Z0-9._-]+\.[a-zA-Z0-9]+$', s))

def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except ValueError:
        return False

def is_valid_yaml(s):
    try:
        yaml.safe_load(s)
        return True
    except yaml.YAMLError:
        return False

def is_valid_xml(s):
    try:
        ET.fromstring(s)
        return True
    except ET.ParseError:
        return False

def is_valid_html(s):
    try:
        soup = BeautifulSoup(s, "html.parser")
        return bool(soup.find())
    except Exception:
        return False
