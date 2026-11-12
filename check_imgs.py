import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
print(f'Total <img> tags in index.html: {len(imgs)}')

missing = []
for src in set(imgs):
    # Normalize path
    local_path = src.replace('/', os.sep)
    exists = os.path.exists(local_path)
    if not exists:
        missing.append(src)
    print(f'{"[OK]" if exists else "[MISSING]"} {src}')

if missing:
    print(f'WARNING: {len(missing)} images missing!')
else:
    print('ALL IMAGES EXIST 100%!')
