import os
import re

base = r"C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website"
html_path = os.path.join(base, "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Check all asset references
assets = re.findall(r'(?:src|href)="([^"]+)"', html)
missing = []
for a in assets:
    if a.startswith("http") or a.startswith("#") or a.startswith("mailto") or a.startswith("tel") or a.startswith("data:"):
        continue
    # Strip any anchors or query params
    clean_a = a.split("?")[0].split("#")[0]
    local_path = os.path.normpath(os.path.join(base, clean_a))
    if not os.path.exists(local_path):
        missing.append((a, local_path))

print(f"Total asset references checked: {len(assets)}")
print(f"Total missing: {len(missing)}")
for m in missing:
    print("MISSING:", m)

# Also check assets in js/script.js
js_path = os.path.join(base, "js", "script.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

js_assets = re.findall(r'assets/images/[a-zA-Z0-9_\-\.]+', js_content)
missing_js = []
for a in set(js_assets):
    local_path = os.path.normpath(os.path.join(base, a))
    if not os.path.exists(local_path):
        missing_js.append((a, local_path))

print(f"Total JS asset references checked: {len(set(js_assets))}")
print(f"Missing JS assets: {len(missing_js)}")
for m in missing_js:
    print("MISSING JS:", m)
