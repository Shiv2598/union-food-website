import urllib.request

try:
    with urllib.request.urlopen('http://localhost:5500/') as res:
        print('HTTP Status:', res.status)
        html = res.read().decode('utf-8')
        print('Bytes received:', len(html))
        print('1. Top bar removed:', ('top-bar' not in html))
        print('2. Hero slider present:', ('hero-slider' in html))
        print('3. Smart search bar in header:', ('nav-search-input' in html))
        print('4. Smart search modal present:', ('modal-search-input' in html))
        print('5. Shifted Food ticker present:', ('food-ticker-section' in html))
        print('6. Official crest logo in navbar:', ('union-foods-logo.png' in html))
        print('7. White logo in footer:', ('union-foods-logo-white.png' in html))
        print('8. Genuine recipe images:', ('food-paneer.jpg' in html and 'food-biryani.jpg' in html))
        print('9. Genuine category cards:', ('cat-oil.jpg' in html and 'cat-flour.jpg' in html))
except Exception as e:
    print('Connection error:', e)
