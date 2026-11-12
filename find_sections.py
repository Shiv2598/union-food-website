with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        lower = line.lower()
        if 'id="recipes"' in lower or 'id="why-choose"' in lower or 'sustainability' in lower or 'certification' in lower:
            print(f'Line {i+1}: {line.strip()[:110]}')
