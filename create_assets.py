import os

output_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\images"
icons_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\icons"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(icons_dir, exist_ok=True)

# 1. Logo
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 60" width="240" height="60">
  <defs>
    <linearGradient id="leafGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4caf50"/>
      <stop offset="100%" stop-color="#2e7d32"/>
    </linearGradient>
    <linearGradient id="leafGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#81c784"/>
      <stop offset="100%" stop-color="#388e3c"/>
    </linearGradient>
    <linearGradient id="brandOrange" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff7a00"/>
      <stop offset="100%" stop-color="#e65100"/>
    </linearGradient>
  </defs>
  <g transform="translate(6, 6) scale(0.9)">
    <path d="M22 6 C12 6 4 16 6 30 C16 30 26 22 26 12 C26 9 24.5 7.2 22 6 Z" fill="url(#leafGrad1)"/>
    <path d="M24 16 C16 18 12 28 14 40 C22 38 30 32 30 22 C30 19 27.5 17.5 24 16 Z" fill="url(#leafGrad2)"/>
    <path d="M8 32 C12 36 20 40 28 42" stroke="#2e7d32" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  </g>
  <text x="52" y="38" font-family="'Poppins', 'Segoe UI', sans-serif" font-weight="800" font-size="28" fill="#1e2229" letter-spacing="-0.5">Union</text>
  <text x="135" y="38" font-family="'Poppins', 'Segoe UI', sans-serif" font-weight="800" font-size="28" fill="url(#brandOrange)" letter-spacing="-0.5">Foods</text>
  <text x="54" y="49" font-family="'Poppins', 'Segoe UI', sans-serif" font-weight="600" font-size="7.5" fill="#2e7d32" letter-spacing="2">PURITY &bull; HEALTH &bull; TRUST</text>
</svg>"""

with open(os.path.join(output_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)

# White Logo for dark backgrounds/footer
logo_white_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 60" width="240" height="60">
  <defs>
    <linearGradient id="leafGradW" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#66bb6a"/>
      <stop offset="100%" stop-color="#43a047"/>
    </linearGradient>
    <linearGradient id="brandOrangeW" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff9800"/>
      <stop offset="100%" stop-color="#f57c00"/>
    </linearGradient>
  </defs>
  <g transform="translate(6, 6) scale(0.9)">
    <path d="M22 6 C12 6 4 16 6 30 C16 30 26 22 26 12 C26 9 24.5 7.2 22 6 Z" fill="url(#leafGradW)"/>
    <path d="M24 16 C16 18 12 28 14 40 C22 38 30 32 30 22 C30 19 27.5 17.5 24 16 Z" fill="#81c784"/>
    <path d="M8 32 C12 36 20 40 28 42" stroke="#66bb6a" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  </g>
  <text x="52" y="38" font-family="'Poppins', 'Segoe UI', sans-serif" font-weight="800" font-size="28" fill="#ffffff" letter-spacing="-0.5">Union</text>
  <text x="135" y="38" font-family="'Poppins', 'Segoe UI', sans-serif" font-weight="800" font-size="28" fill="url(#brandOrangeW)" letter-spacing="-0.5">Foods</text>
  <text x="54" y="49" font-family="'Poppins', 'Segoe UI', sans-serif" font-weight="600" font-size="7.5" fill="#a5d6a7" letter-spacing="2">PURITY &bull; HEALTH &bull; TRUST</text>
</svg>"""

with open(os.path.join(output_dir, "logo-white.svg"), "w", encoding="utf-8") as f:
    f.write(logo_white_svg)

# 2. Product 1: Refined Sunflower Oil
oil_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="oilBody" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f5a623"/>
      <stop offset="30%" stop-color="#ffd15c"/>
      <stop offset="70%" stop-color="#ffb700"/>
      <stop offset="100%" stop-color="#d98200"/>
    </linearGradient>
    <linearGradient id="bottleShine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.7)"/>
      <stop offset="50%" stop-color="rgba(255,255,255,0.1)"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(0,0,0,0.12)"/>
    </filter>
  </defs>
  <circle cx="150" cy="200" r="140" fill="#fff9e6"/>
  <!-- Bottle Cap -->
  <rect x="132" y="30" width="36" height="24" rx="4" fill="#ff7a00"/>
  <rect x="135" y="34" width="30" height="4" fill="#ffa726"/>
  <rect x="135" y="42" width="30" height="4" fill="#ffa726"/>
  <!-- Bottle Neck -->
  <path d="M136 54 L164 54 L170 85 L130 85 Z" fill="#fff3c4" stroke="#e0a020" stroke-width="1.5"/>
  <!-- Bottle Body -->
  <path d="M130 85 C100 95 90 125 90 150 L90 320 C90 345 110 355 150 355 C190 355 210 345 210 320 L210 150 C210 125 200 95 170 85 Z" fill="url(#oilBody)" filter="url(#cardShadow)"/>
  <!-- Bottle Highlights -->
  <path d="M96 150 L96 315 C96 335 115 345 150 345" fill="none" stroke="url(#bottleShine)" stroke-width="10" stroke-linecap="round"/>
  <!-- Bottle Label -->
  <rect x="100" y="185" width="100" height="105" rx="6" fill="#ffffff" stroke="#e0e0e0" stroke-width="1"/>
  <g transform="translate(105, 190)">
    <path d="M45 4 C40 4 36 8 37 13 C41 13 45 10 45 6 Z" fill="#388e3c"/>
    <text x="45" y="24" font-family="'Poppins', sans-serif" font-weight="800" font-size="10" fill="#e65100" text-anchor="middle">Union Foods</text>
    <text x="45" y="36" font-family="'Poppins', sans-serif" font-weight="700" font-size="8.5" fill="#1b5e20" text-anchor="middle">Refined</text>
    <text x="45" y="48" font-family="'Poppins', sans-serif" font-weight="800" font-size="9" fill="#d84315" text-anchor="middle">Sunflower Oil</text>
    <circle cx="45" cy="70" r="14" fill="#f57f17"/>
    <circle cx="45" cy="70" r="7" fill="#5d4037"/>
    <g fill="#fbc02d">
      <ellipse cx="45" cy="52" rx="3" ry="5"/>
      <ellipse cx="45" cy="88" rx="3" ry="5"/>
      <ellipse cx="27" cy="70" rx="5" ry="3"/>
      <ellipse cx="63" cy="70" rx="5" ry="3"/>
      <circle cx="33" cy="58" r="3"/>
      <circle cx="57" cy="58" r="3"/>
      <circle cx="33" cy="82" r="3"/>
      <circle cx="57" cy="82" r="3"/>
    </g>
    <text x="45" y="96" font-family="'Poppins', sans-serif" font-weight="700" font-size="6.5" fill="#2e7d32" text-anchor="middle">100% PURE &bull; LIGHT &bull; HEALTHY</text>
  </g>
  <rect x="125" y="310" width="50" height="20" rx="10" fill="#e65100"/>
  <text x="150" y="324" font-family="'Poppins', sans-serif" font-weight="800" font-size="11" fill="#ffffff" text-anchor="middle">1 Litre</text>
</svg>"""

with open(os.path.join(output_dir, "sunflower-oil.svg"), "w", encoding="utf-8") as f:
    f.write(oil_svg)

# 3. Product 2: Premium Atta
atta_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="attaBag" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fffdf7"/>
      <stop offset="60%" stop-color="#f5e8cf"/>
      <stop offset="100%" stop-color="#e8d3ad"/>
    </linearGradient>
    <linearGradient id="attaGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff9100"/>
      <stop offset="100%" stop-color="#e65100"/>
    </linearGradient>
    <filter id="bagShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(0,0,0,0.12)"/>
    </filter>
  </defs>
  <circle cx="150" cy="200" r="140" fill="#fdfbf2"/>
  <path d="M85 80 C110 70 190 70 215 80 L230 330 C230 350 200 360 150 360 C100 360 70 350 70 330 Z" fill="url(#attaBag)" stroke="#d4b584" stroke-width="2" filter="url(#bagShadow)"/>
  <line x1="85" y1="88" x2="215" y2="88" stroke="#8d6e63" stroke-width="3" stroke-dasharray="6,4"/>
  <rect x="75" y="115" width="150" height="38" fill="url(#attaGold)"/>
  <text x="150" y="130" font-family="'Poppins', sans-serif" font-weight="700" font-size="10" fill="#ffffff" text-anchor="middle" letter-spacing="1">UNION FOODS</text>
  <text x="150" y="145" font-family="'Poppins', sans-serif" font-weight="800" font-size="13" fill="#fff9c4" text-anchor="middle">PREMIUM SHARBATI</text>
  <text x="150" y="205" font-family="'Playfair Display', Georgia, serif" font-weight="900" font-size="52" fill="#5d4037" text-anchor="middle">Atta</text>
  <text x="150" y="225" font-family="'Poppins', sans-serif" font-weight="600" font-size="11" fill="#795548" text-anchor="middle">100% Whole Wheat Chakki Fresh</text>
  <!-- Wheat Graphic -->
  <g transform="translate(150, 255) scale(1.1)">
    <path d="M0 -15 C-5 -10 -5 10 0 15 C5 10 5 -10 0 -15" fill="#f57f17"/>
    <path d="M-8 -6 C-12 -2 -10 8 -4 8 C-2 4 -4 -2 -8 -6" fill="#fbc02d"/>
    <path d="M8 -6 C12 -2 10 8 4 8 C2 4 4 -2 8 -6" fill="#fbc02d"/>
    <path d="M-10 6 C-14 10 -12 18 -6 18 C-4 14 -6 10 -10 6" fill="#fbc02d"/>
    <path d="M10 6 C14 10 12 18 6 18 C4 14 6 10 10 6" fill="#fbc02d"/>
    <line x1="0" y1="15" x2="0" y2="40" stroke="#f57f17" stroke-width="2.5"/>
  </g>
  <rect x="120" y="325" width="60" height="22" rx="11" fill="#e65100"/>
  <text x="150" y="340" font-family="'Poppins', sans-serif" font-weight="800" font-size="12" fill="#ffffff" text-anchor="middle">5 Kg</text>
</svg>"""

with open(os.path.join(output_dir, "premium-atta.svg"), "w", encoding="utf-8") as f:
    f.write(atta_svg)

# 4. Product 3: Moong Dal
moong_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="moongPack" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2e7d32"/>
      <stop offset="50%" stop-color="#388e3c"/>
      <stop offset="100%" stop-color="#1b5e20"/>
    </linearGradient>
    <filter id="packShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(0,0,0,0.15)"/>
    </filter>
  </defs>
  <circle cx="150" cy="200" r="140" fill="#f1f8e9"/>
  <path d="M80 75 L220 75 L235 330 C235 348 215 358 150 358 C85 358 65 348 65 330 Z" fill="url(#moongPack)" filter="url(#packShadow)"/>
  <rect x="75" y="70" width="150" height="15" rx="4" fill="#1b5e20"/>
  <line x1="80" y1="80" x2="220" y2="80" stroke="#81c784" stroke-width="2" stroke-dasharray="4,3"/>
  <rect x="95" y="98" width="110" height="26" rx="13" fill="#ffffff"/>
  <text x="150" y="115" font-family="'Poppins', sans-serif" font-weight="800" font-size="11" fill="#e65100" text-anchor="middle">Union Foods</text>
  <text x="150" y="160" font-family="'Poppins', sans-serif" font-weight="900" font-size="28" fill="#ffffff" text-anchor="middle">Moong</text>
  <text x="150" y="188" font-family="'Poppins', sans-serif" font-weight="800" font-size="24" fill="#ffeb3b" text-anchor="middle">Dal</text>
  <text x="150" y="205" font-family="'Poppins', sans-serif" font-weight="600" font-size="9" fill="#c8e6c9" text-anchor="middle" letter-spacing="1">UNPOLISHED &bull; HIGH PROTEIN</text>
  <ellipse cx="150" cy="260" rx="55" ry="38" fill="#ffffff" stroke="#c8e6c9" stroke-width="4"/>
  <g fill="#fdd835">
    <ellipse cx="130" cy="250" rx="9" ry="6"/>
    <ellipse cx="150" cy="245" rx="8" ry="5"/>
    <ellipse cx="170" cy="252" rx="9" ry="6"/>
    <ellipse cx="125" cy="265" rx="8" ry="6"/>
    <ellipse cx="145" cy="262" rx="10" ry="7"/>
    <ellipse cx="165" cy="266" rx="8" ry="5"/>
    <ellipse cx="138" cy="275" rx="8" ry="5"/>
    <ellipse cx="158" cy="278" rx="9" ry="6"/>
  </g>
  <rect x="120" y="318" width="60" height="22" rx="11" fill="#ff9800"/>
  <text x="150" y="333" font-family="'Poppins', sans-serif" font-weight="800" font-size="12" fill="#ffffff" text-anchor="middle">1 Kg</text>
</svg>"""

with open(os.path.join(output_dir, "moong-dal.svg"), "w", encoding="utf-8") as f:
    f.write(moong_svg)

# 5. Product 4: Chana Dal
chana_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="chanaPack" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c62828"/>
      <stop offset="50%" stop-color="#b71c1c"/>
      <stop offset="100%" stop-color="#880e4f"/>
    </linearGradient>
    <filter id="chanaShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(0,0,0,0.15)"/>
    </filter>
  </defs>
  <circle cx="150" cy="200" r="140" fill="#fbe9e7"/>
  <path d="M80 75 L220 75 L235 330 C235 348 215 358 150 358 C85 358 65 348 65 330 Z" fill="url(#chanaPack)" filter="url(#chanaShadow)"/>
  <rect x="75" y="70" width="150" height="15" rx="4" fill="#7f0000"/>
  <line x1="80" y1="80" x2="220" y2="80" stroke="#ff8a80" stroke-width="2" stroke-dasharray="4,3"/>
  <rect x="95" y="98" width="110" height="26" rx="13" fill="#ffffff"/>
  <text x="150" y="115" font-family="'Poppins', sans-serif" font-weight="800" font-size="11" fill="#e65100" text-anchor="middle">Union Foods</text>
  <text x="150" y="160" font-family="'Poppins', sans-serif" font-weight="900" font-size="28" fill="#ffffff" text-anchor="middle">Chana</text>
  <text x="150" y="188" font-family="'Poppins', sans-serif" font-weight="800" font-size="24" fill="#ffe082" text-anchor="middle">Dal</text>
  <text x="150" y="205" font-family="'Poppins', sans-serif" font-weight="600" font-size="9" fill="#ffcdd2" text-anchor="middle" letter-spacing="1">100% NATURAL &bull; DESI CHANA</text>
  <ellipse cx="150" cy="260" rx="55" ry="38" fill="#ffffff" stroke="#ffcdd2" stroke-width="4"/>
  <g fill="#f57c00">
    <circle cx="132" cy="252" r="7"/>
    <circle cx="150" cy="246" r="8"/>
    <circle cx="168" cy="253" r="7.5"/>
    <circle cx="124" cy="266" r="7"/>
    <circle cx="144" cy="264" r="8.5"/>
    <circle cx="165" cy="268" r="7"/>
    <circle cx="136" cy="276" r="7"/>
    <circle cx="156" cy="278" r="8"/>
  </g>
  <rect x="120" y="318" width="60" height="22" rx="11" fill="#ff9800"/>
  <text x="150" y="333" font-family="'Poppins', sans-serif" font-weight="800" font-size="12" fill="#ffffff" text-anchor="middle">1 Kg</text>
</svg>"""

with open(os.path.join(output_dir, "chana-dal.svg"), "w", encoding="utf-8") as f:
    f.write(chana_svg)

# 6. Hero Products Showcase Group
hero_showcase_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 500" width="700" height="500">
  <defs>
    <radialGradient id="sunGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#fff8e1" stop-opacity="0.95"/>
      <stop offset="60%" stop-color="#ffe082" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ffb300" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="350" cy="250" r="230" fill="url(#sunGlow)"/>
  
  <g stroke="#ffb300" stroke-width="2" opacity="0.6">
    <path d="M60 480 Q100 360 120 300 M120 300 L110 280 M120 300 L130 280 M115 320 L100 310 M125 320 L140 310"/>
    <path d="M140 480 Q170 380 190 320 M190 320 L180 300 M190 320 L200 300"/>
    <path d="M520 480 Q500 370 480 300 M480 300 L470 280 M480 300 L490 280"/>
    <path d="M600 480 Q570 360 550 310 M550 310 L540 290 M550 310 L560 290"/>
  </g>

  <!-- Left: Oil Bottle -->
  <g transform="translate(130, 80) scale(0.66)">
    <image href="sunflower-oil.svg" width="300" height="400"/>
  </g>

  <!-- Center: Atta Bag -->
  <g transform="translate(255, 60) scale(0.74)">
    <image href="premium-atta.svg" width="300" height="400"/>
  </g>

  <!-- Center Right: Moong Dal -->
  <g transform="translate(400, 105) scale(0.62)">
    <image href="moong-dal.svg" width="300" height="400"/>
  </g>

  <!-- Far Right: Chana Dal -->
  <g transform="translate(500, 125) scale(0.56)">
    <image href="chana-dal.svg" width="300" height="400"/>
  </g>

  <ellipse cx="350" cy="455" rx="320" ry="35" fill="#fdfaf0" opacity="0.95"/>
  <ellipse cx="340" cy="445" rx="70" ry="18" fill="#fff8e1"/>
  <path d="M305 440 C305 460 375 460 375 440 Z" fill="#d7ccc8" stroke="#8d6e63" stroke-width="2"/>
  <ellipse cx="340" cy="440" rx="35" ry="10" fill="#ffffff"/>
  <g fill="#f57f17">
    <ellipse cx="230" cy="448" rx="5" ry="2.5" transform="rotate(20 230 448)"/>
    <ellipse cx="245" cy="452" rx="6" ry="3" transform="rotate(-15 245 452)"/>
    <ellipse cx="260" cy="446" rx="5" ry="2.5" transform="rotate(40 260 446)"/>
    <ellipse cx="420" cy="450" rx="5" ry="2.5" transform="rotate(-30 420 450)"/>
    <ellipse cx="440" cy="454" rx="6" ry="3" transform="rotate(10 440 454)"/>
    <ellipse cx="460" cy="448" rx="5" ry="2.5" transform="rotate(-20 460 448)"/>
  </g>
</svg>"""

with open(os.path.join(output_dir, "hero-showcase.svg"), "w", encoding="utf-8") as f:
    f.write(hero_showcase_svg)

# 7. Modern Corporate Processing Facility
facility_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="600" height="400">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="60%" stop-color="#bae6fd"/>
      <stop offset="100%" stop-color="#f0f9ff"/>
    </linearGradient>
    <linearGradient id="facGlass" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#e0f2fe"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="wallGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#cbd5e1"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="600" height="400" fill="url(#skyGrad)"/>
  <circle cx="480" cy="70" r="45" fill="#fff" opacity="0.8"/>
  <ellipse cx="120" cy="80" rx="60" ry="20" fill="#ffffff" opacity="0.7"/>
  <ellipse cx="160" cy="75" rx="40" ry="25" fill="#ffffff" opacity="0.8"/>
  <path d="M0 240 Q150 200 320 230 T600 220 L600 400 L0 400 Z" fill="#86efac" opacity="0.4"/>
  <polygon points="50,210 160,190 160,330 50,340" fill="#e2e8f0" stroke="#94a3b8"/>
  <polygon points="160,160 440,160 440,330 160,330" fill="url(#wallGrad)" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="440,185 550,205 550,335 440,330" fill="#e2e8f0" stroke="#94a3b8"/>
  <rect x="155" y="150" width="290" height="24" fill="#0f172a"/>
  <!-- Union Foods Signage on Building -->
  <rect x="230" y="180" width="140" height="36" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>
  <text x="258" y="204" font-family="'Poppins', sans-serif" font-weight="900" font-size="16" fill="#1e293b">Union</text>
  <text x="312" y="204" font-family="'Poppins', sans-serif" font-weight="900" font-size="16" fill="#ea580c">Foods</text>
  <circle cx="245" cy="198" r="6" fill="#22c55e"/>

  <g fill="url(#facGlass)" opacity="0.85">
    <rect x="180" y="230" width="45" height="35" rx="2"/>
    <rect x="235" y="230" width="45" height="35" rx="2"/>
    <rect x="290" y="230" width="45" height="35" rx="2"/>
    <rect x="345" y="230" width="45" height="35" rx="2"/>
    <rect x="400" y="230" width="25" height="35" rx="2"/>
    
    <rect x="180" y="275" width="45" height="40" rx="2"/>
    <rect x="235" y="275" width="45" height="40" rx="2"/>
    <rect x="345" y="275" width="45" height="40" rx="2"/>
    <rect x="400" y="275" width="25" height="40" rx="2"/>
  </g>
  <rect x="290" y="275" width="45" height="55" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
  <rect x="280" y="270" width="65" height="6" fill="#ea580c"/>

  <path d="M0 330 C150 325 450 325 600 330 L600 400 L0 400 Z" fill="#22c55e"/>
  <polygon points="260,400 340,400 320,330 280,330" fill="#94a3b8"/>
  <g fill="#15803d">
    <circle cx="80" cy="335" r="16"/>
    <circle cx="110" cy="335" r="14"/>
    <circle cx="140" cy="335" r="18"/>
    <circle cx="460" cy="335" r="18"/>
    <circle cx="490" cy="335" r="15"/>
    <circle cx="520" cy="335" r="17"/>
  </g>
</svg>"""

with open(os.path.join(output_dir, "facility.svg"), "w", encoding="utf-8") as f:
    f.write(facility_svg)

# 8. Recipe Dish
curry_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 550 350" width="550" height="350">
  <defs>
    <radialGradient id="curryGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff7043"/>
      <stop offset="60%" stop-color="#d84315"/>
      <stop offset="100%" stop-color="#bf360c"/>
    </radialGradient>
    <linearGradient id="rotiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff8e1"/>
      <stop offset="50%" stop-color="#ffe082"/>
      <stop offset="100%" stop-color="#ffb74d"/>
    </linearGradient>
    <filter id="curryGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="15" flood-color="rgba(0,0,0,0.3)"/>
    </filter>
  </defs>
  <rect x="0" y="0" width="550" height="350" fill="#2d1e18" rx="16"/>
  
  <ellipse cx="430" cy="190" rx="95" ry="60" fill="#4e342e"/>
  <ellipse cx="430" cy="180" rx="88" ry="52" fill="url(#rotiGrad)" filter="url(#curryGlow)"/>
  <g fill="#8d6e63" opacity="0.6">
    <circle cx="400" cy="165" r="5"/>
    <circle cx="420" cy="185" r="8"/>
    <circle cx="445" cy="160" r="6"/>
    <circle cx="460" cy="195" r="7"/>
    <circle cx="390" cy="190" r="4"/>
  </g>
  <ellipse cx="425" cy="175" rx="30" ry="15" fill="#fff9c4" opacity="0.6"/>

  <g filter="url(#curryGlow)">
    <ellipse cx="210" cy="185" rx="130" ry="85" fill="#3e2723"/>
    <ellipse cx="210" cy="180" rx="122" ry="78" fill="#5d4037"/>
    <ellipse cx="210" cy="180" rx="114" ry="70" fill="url(#curryGrad)"/>
    <g>
      <rect x="170" y="160" width="22" height="18" rx="3" fill="#fffde7" stroke="#ffcc80"/>
      <rect x="220" y="150" width="25" height="20" rx="3" fill="#fffde7" stroke="#ffcc80"/>
      <rect x="200" y="185" width="24" height="19" rx="3" fill="#fffde7" stroke="#ffcc80"/>
      <rect x="250" y="175" width="20" height="16" rx="3" fill="#fffde7" stroke="#ffcc80"/>
      <circle cx="155" cy="180" r="7" fill="#4caf50"/>
      <circle cx="190" cy="150" r="6.5" fill="#4caf50"/>
      <circle cx="230" cy="195" r="7" fill="#4caf50"/>
      <circle cx="270" cy="165" r="6.5" fill="#4caf50"/>
      <polygon points="175,190 190,185 185,200" fill="#e53935"/>
      <polygon points="215,140 230,135 225,148" fill="#e53935"/>
      <polygon points="250,195 265,190 260,205" fill="#e53935"/>
      <path d="M205 170 Q215 160 210 150 Q218 165 225 172" stroke="#2e7d32" stroke-width="2.5" fill="none"/>
      <circle cx="206" cy="152" r="3" fill="#66bb6a"/>
      <circle cx="220" cy="168" r="3" fill="#66bb6a"/>
      <path d="M165 175 C190 195 230 160 255 180" stroke="#fff9c4" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.8"/>
    </g>
  </g>

  <path d="M190 120 Q180 90 200 65" stroke="#ffffff" stroke-width="2" fill="none" opacity="0.4" stroke-linecap="round"/>
  <path d="M220 115 Q235 85 225 60" stroke="#ffffff" stroke-width="2.5" fill="none" opacity="0.5" stroke-linecap="round"/>
  <path d="M250 125 Q240 95 255 70" stroke="#ffffff" stroke-width="2" fill="none" opacity="0.4" stroke-linecap="round"/>
</svg>"""

with open(os.path.join(output_dir, "recipe-curry.svg"), "w", encoding="utf-8") as f:
    f.write(curry_svg)

# 9. Category SVGs
categories = {
    "cat-cooking-oil.svg": ("#fff8e1", "#f59e0b", """
      <path d="M40 20 L60 20 L65 40 L35 40 Z" fill="#f59e0b"/>
      <rect x="30" y="40" width="40" height="55" rx="8" fill="#fbbf24"/>
      <circle cx="50" cy="65" r="12" fill="#d97706"/>
      <circle cx="50" cy="65" r="5" fill="#78350f"/>
    """),
    "cat-flour-grains.svg": ("#fefce8", "#ca8a04", """
      <ellipse cx="50" cy="70" rx="35" ry="14" fill="#a16207"/>
      <path d="M15 70 C15 90 85 90 85 70 Z" fill="#78350f"/>
      <ellipse cx="50" cy="68" rx="32" ry="12" fill="#fef08a"/>
      <path d="M50 20 L50 55 M42 30 L50 22 L58 30 M42 42 L50 34 L58 42" stroke="#ca8a04" stroke-width="2.5" stroke-linecap="round"/>
    """),
    "cat-pulses-dal.svg": ("#f0fdf4", "#16a34a", """
      <ellipse cx="35" cy="55" rx="20" ry="12" fill="#ca8a04"/>
      <ellipse cx="65" cy="55" rx="20" ry="12" fill="#dc2626"/>
      <ellipse cx="50" cy="72" rx="24" ry="14" fill="#16a34a"/>
      <circle cx="50" cy="40" r="10" fill="#facc15"/>
    """),
    "cat-spices.svg": ("#fff1f2", "#e11d48", """
      <circle cx="35" cy="55" r="18" fill="#e11d48"/>
      <circle cx="65" cy="55" r="18" fill="#ea580c"/>
      <circle cx="50" cy="72" r="18" fill="#eab308"/>
      <path d="M48 20 C40 25 35 32 40 38 C45 34 55 24 48 20 Z" fill="#16a34a"/>
    """),
    "cat-snacks.svg": ("#fff7ed", "#ea580c", """
      <ellipse cx="50" cy="75" rx="35" ry="12" fill="#c2410c"/>
      <path d="M30 40 L45 25 L60 40 L70 55 L30 55 Z" fill="#f97316"/>
      <polygon points="35,60 50,45 65,60" fill="#fbbf24"/>
      <polygon points="45,45 58,32 72,48" fill="#f59e0b"/>
    """),
    "cat-beverages.svg": ("#fef9c3", "#ca8a04", """
      <polygon points="35,25 65,25 58,80 42,80" fill="#fde047" stroke="#eab308" stroke-width="2"/>
      <line x1="50" y1="12" x2="62" y2="50" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
      <circle cx="35" cy="30" r="12" fill="#84cc16"/>
    """),
    "cat-packaged-foods.svg": ("#fafaf9", "#78716c", """
      <rect x="25" y="30" width="50" height="55" rx="6" fill="#0284c7"/>
      <rect x="32" y="42" width="36" height="22" rx="3" fill="#ffffff"/>
      <circle cx="50" cy="53" r="6" fill="#f97316"/>
      <rect x="28" y="25" width="44" height="8" rx="2" fill="#0369a1"/>
    """)
}

for fname, (bg, accent, content) in categories.items():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
      <circle cx="50" cy="50" r="46" fill="{bg}" stroke="{accent}" stroke-width="1.5"/>
      {content}
    </svg>"""
    with open(os.path.join(output_dir, fname), "w", encoding="utf-8") as f:
        f.write(svg)

# 10. Certifications
fssai_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <circle cx="80" cy="80" r="74" fill="#ffffff" stroke="#1d4ed8" stroke-width="4"/>
  <circle cx="80" cy="80" r="66" fill="#eff6ff"/>
  <text x="80" y="70" font-family="'Poppins', sans-serif" font-weight="900" font-size="28" fill="#1d4ed8" text-anchor="middle" letter-spacing="1">fssai</text>
  <line x1="30" y1="82" x2="130" y2="82" stroke="#ea580c" stroke-width="3"/>
  <text x="80" y="98" font-family="'Poppins', sans-serif" font-weight="700" font-size="8.5" fill="#1e293b" text-anchor="middle">LIC NO. 12026999000142</text>
  <text x="80" y="112" font-family="'Poppins', sans-serif" font-weight="800" font-size="8" fill="#15803d" text-anchor="middle">100% FOOD SAFETY</text>
  <path d="M80 120 L84 128 L93 129 L86 135 L88 144 L80 139 L72 144 L74 135 L67 129 L76 128 Z" fill="#ea580c"/>
</svg>"""

with open(os.path.join(output_dir, "cert-fssai.svg"), "w", encoding="utf-8") as f:
    f.write(fssai_svg)

iso_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <circle cx="80" cy="80" r="74" fill="#ffffff" stroke="#0284c7" stroke-width="4"/>
  <circle cx="80" cy="80" r="66" fill="#f0f9ff"/>
  <text x="80" y="65" font-family="'Poppins', sans-serif" font-weight="900" font-size="32" fill="#0369a1" text-anchor="middle">ISO</text>
  <rect x="35" y="75" width="90" height="20" rx="4" fill="#0284c7"/>
  <text x="80" y="89" font-family="'Poppins', sans-serif" font-weight="800" font-size="11" fill="#ffffff" text-anchor="middle">9001 : 2015</text>
  <text x="80" y="112" font-family="'Poppins', sans-serif" font-weight="700" font-size="8.5" fill="#0369a1" text-anchor="middle">&amp; ISO 22000 FSMS</text>
  <text x="80" y="125" font-family="'Poppins', sans-serif" font-weight="600" font-size="7.5" fill="#64748b" text-anchor="middle">CERTIFIED QUALITY</text>
</svg>"""

with open(os.path.join(output_dir, "cert-iso.svg"), "w", encoding="utf-8") as f:
    f.write(iso_svg)

haccp_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <circle cx="80" cy="80" r="74" fill="#ffffff" stroke="#16a34a" stroke-width="4"/>
  <circle cx="80" cy="80" r="66" fill="#f0fdf4"/>
  <circle cx="80" cy="80" r="54" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="80" y="75" font-family="'Poppins', sans-serif" font-weight="900" font-size="24" fill="#15803d" text-anchor="middle" letter-spacing="1">HACCP</text>
  <text x="80" y="94" font-family="'Poppins', sans-serif" font-weight="800" font-size="10" fill="#166534" text-anchor="middle">CERTIFIED</text>
  <text x="80" y="112" font-family="'Poppins', sans-serif" font-weight="600" font-size="7.5" fill="#15803d" text-anchor="middle">HAZARD ANALYSIS</text>
  <text x="80" y="122" font-family="'Poppins', sans-serif" font-weight="600" font-size="7.5" fill="#15803d" text-anchor="middle">&amp; CRITICAL CONTROL</text>
</svg>"""

with open(os.path.join(output_dir, "cert-haccp.svg"), "w", encoding="utf-8") as f:
    f.write(haccp_svg)

# 11. Customer Avatar
avatar_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <clipPath id="circleClip">
      <circle cx="60" cy="60" r="56"/>
    </clipPath>
  </defs>
  <circle cx="60" cy="60" r="58" fill="#ea580c"/>
  <g clip-path="url(#circleClip)">
    <rect x="0" y="0" width="120" height="120" fill="#fef3c7"/>
    <path d="M15 130 C20 95 40 85 60 85 C80 85 100 95 105 130 Z" fill="#d97706"/>
    <rect x="52" y="65" width="16" height="25" fill="#d49a75"/>
    <ellipse cx="60" cy="50" rx="22" ry="26" fill="#e8b593"/>
    <path d="M35 55 C32 30 45 15 60 15 C75 15 88 30 85 55 C82 50 78 40 60 40 C42 40 38 50 35 55 Z" fill="#292524"/>
    <path d="M35 50 C32 65 35 85 42 90 C40 80 40 65 42 55 Z" fill="#292524"/>
    <path d="M85 50 C88 65 85 85 78 90 C80 80 80 65 78 55 Z" fill="#292524"/>
    <circle cx="52" cy="48" r="2.5" fill="#1c1917"/>
    <circle cx="68" cy="48" r="2.5" fill="#1c1917"/>
    <circle cx="60" cy="44" r="1.5" fill="#dc2626"/>
    <path d="M54 58 Q60 64 66 58" stroke="#b91c1c" stroke-width="2" fill="none" stroke-linecap="round"/>
  </g>
</svg>"""

with open(os.path.join(output_dir, "priya-avatar.svg"), "w", encoding="utf-8") as f:
    f.write(avatar_svg)

# 12. News Thumbnails
news1_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 140" width="200" height="140">
  <rect x="0" y="0" width="200" height="140" fill="#e2e8f0"/>
  <rect x="20" y="30" width="160" height="60" fill="#94a3b8"/>
  <rect x="30" y="15" width="20" height="25" fill="#64748b"/>
  <rect x="50" y="70" width="80" height="40" rx="3" fill="#ea580c"/>
  <polygon points="130,80 150,80 155,100 155,110 130,110" fill="#f97316"/>
  <circle cx="75" cy="115" r="12" fill="#1e293b"/>
  <circle cx="138" cy="115" r="12" fill="#1e293b"/>
  <rect x="55" y="78" width="50" height="15" rx="2" fill="#ffffff"/>
  <text x="80" y="90" font-family="'Poppins', sans-serif" font-weight="900" font-size="8" fill="#ea580c" text-anchor="middle">UNION FOODS</text>
  <rect x="0" y="125" width="200" height="15" fill="#475569"/>
</svg>"""

with open(os.path.join(output_dir, "news-fleet.svg"), "w", encoding="utf-8") as f:
    f.write(news1_svg)

news2_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 140" width="200" height="140">
  <rect x="0" y="0" width="200" height="140" fill="#bbf7d0"/>
  <ellipse cx="100" cy="120" rx="80" ry="30" fill="#78350f"/>
  <path d="M40 100 C60 120 90 125 100 115" stroke="#d49a75" stroke-width="12" stroke-linecap="round" fill="none"/>
  <path d="M160 100 C140 120 110 125 100 115" stroke="#d49a75" stroke-width="12" stroke-linecap="round" fill="none"/>
  <path d="M100 110 L100 70" stroke="#15803d" stroke-width="4" stroke-linecap="round"/>
  <path d="M100 80 C85 75 75 60 85 45 C95 45 100 65 100 80 Z" fill="#22c55e"/>
  <path d="M100 75 C115 70 125 55 115 40 C105 40 100 60 100 75 Z" fill="#4ade80"/>
  <circle cx="100" cy="35" r="4" fill="#86efac"/>
</svg>"""

with open(os.path.join(output_dir, "news-green.svg"), "w", encoding="utf-8") as f:
    f.write(news2_svg)

print("All vector assets created successfully!")
