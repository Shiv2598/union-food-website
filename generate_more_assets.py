import os

output_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\images"
icons_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\icons"

# Additional Product SVGs for Catalog:
# 1. Mustard Oil
mustard_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="mustardGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="35%" stop-color="#f59e0b"/>
      <stop offset="70%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
    <filter id="mDrop" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(0,0,0,0.15)"/>
    </filter>
  </defs>
  <circle cx="150" cy="200" r="140" fill="#fef3c7"/>
  <rect x="132" y="30" width="36" height="24" rx="4" fill="#15803d"/>
  <path d="M136 54 L164 54 L170 85 L130 85 Z" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
  <path d="M130 85 C100 95 90 125 90 150 L90 320 C90 345 110 355 150 355 C190 355 210 345 210 320 L210 150 C210 125 200 95 170 85 Z" fill="url(#mustardGrad)" filter="url(#mDrop)"/>
  <rect x="100" y="185" width="100" height="105" rx="6" fill="#ffffff" stroke="#e2e8f0"/>
  <g transform="translate(105, 190)">
    <text x="45" y="24" font-family="'Poppins', sans-serif" font-weight="800" font-size="10" fill="#ea580c" text-anchor="middle">Union Foods</text>
    <text x="45" y="38" font-family="'Poppins', sans-serif" font-weight="700" font-size="9" fill="#166534" text-anchor="middle">Kachi Ghani</text>
    <text x="45" y="52" font-family="'Poppins', sans-serif" font-weight="800" font-size="9.5" fill="#b45309" text-anchor="middle">Mustard Oil</text>
    <circle cx="45" cy="74" r="12" fill="#fef08a" stroke="#ca8a04"/>
    <circle cx="45" cy="74" r="5" fill="#78350f"/>
    <text x="45" y="96" font-family="'Poppins', sans-serif" font-weight="700" font-size="6.5" fill="#15803d" text-anchor="middle">COLD PRESSED &bull; PURE</text>
  </g>
  <rect x="125" y="312" width="50" height="20" rx="10" fill="#15803d"/>
  <text x="150" y="326" font-family="'Poppins', sans-serif" font-weight="800" font-size="11" fill="#ffffff" text-anchor="middle">1 Litre</text>
</svg>"""

with open(os.path.join(output_dir, "mustard-oil.svg"), "w", encoding="utf-8") as f:
    f.write(mustard_svg)

# 2. Toor Dal
toor_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="toorPack" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <filter id="tDrop" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="rgba(0,0,0,0.15)"/>
    </filter>
  </defs>
  <circle cx="150" cy="200" r="140" fill="#fffbeb"/>
  <path d="M80 75 L220 75 L235 330 C235 348 215 358 150 358 C85 358 65 348 65 330 Z" fill="url(#toorPack)" filter="url(#tDrop)"/>
  <rect x="75" y="70" width="150" height="15" rx="4" fill="#78350f"/>
  <rect x="95" y="98" width="110" height="26" rx="13" fill="#ffffff"/>
  <text x="150" y="115" font-family="'Poppins', sans-serif" font-weight="800" font-size="11" fill="#ea580c" text-anchor="middle">Union Foods</text>
  <text x="150" y="160" font-family="'Poppins', sans-serif" font-weight="900" font-size="28" fill="#ffffff" text-anchor="middle">Toor</text>
  <text x="150" y="188" font-family="'Poppins', sans-serif" font-weight="800" font-size="24" fill="#fef08a" text-anchor="middle">Dal</text>
  <text x="150" y="205" font-family="'Poppins', sans-serif" font-weight="600" font-size="9" fill="#fef3c7" text-anchor="middle">UNPOLISHED DESI TOOR</text>
  <ellipse cx="150" cy="260" rx="55" ry="38" fill="#ffffff" stroke="#fef08a" stroke-width="4"/>
  <g fill="#eab308">
    <circle cx="132" cy="252" r="7"/>
    <circle cx="150" cy="246" r="8"/>
    <circle cx="168" cy="253" r="7.5"/>
    <circle cx="124" cy="266" r="7"/>
    <circle cx="144" cy="264" r="8.5"/>
    <circle cx="165" cy="268" r="7"/>
    <circle cx="136" cy="276" r="7"/>
    <circle cx="156" cy="278" r="8"/>
  </g>
  <rect x="120" y="318" width="60" height="22" rx="11" fill="#b45309"/>
  <text x="150" y="333" font-family="'Poppins', sans-serif" font-weight="800" font-size="12" fill="#ffffff" text-anchor="middle">1 Kg</text>
</svg>"""

with open(os.path.join(output_dir, "toor-dal.svg"), "w", encoding="utf-8") as f:
    f.write(toor_svg)

# 3. Turmeric Powder (Spices)
haldi_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 400" width="300" height="400">
  <defs>
    <linearGradient id="haldiPack" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#facc15"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#ca8a04"/>
    </linearGradient>
  </defs>
  <circle cx="150" cy="200" r="140" fill="#fef9c3"/>
  <path d="M80 75 L220 75 L235 330 C235 348 215 358 150 358 C85 358 65 348 65 330 Z" fill="url(#haldiPack)"/>
  <rect x="75" y="70" width="150" height="15" rx="4" fill="#a16207"/>
  <rect x="95" y="98" width="110" height="26" rx="13" fill="#ffffff"/>
  <text x="150" y="115" font-family="'Poppins', sans-serif" font-weight="800" font-size="11" fill="#ea580c" text-anchor="middle">Union Foods</text>
  <text x="150" y="160" font-family="'Poppins', sans-serif" font-weight="900" font-size="26" fill="#78350f" text-anchor="middle">Haldi Powder</text>
  <text x="150" y="184" font-family="'Poppins', sans-serif" font-weight="700" font-size="14" fill="#ffffff" text-anchor="middle">Pure Turmeric</text>
  <text x="150" y="205" font-family="'Poppins', sans-serif" font-weight="600" font-size="9" fill="#78350f" text-anchor="middle">HIGH CURCUMIN &bull; NO COLOR</text>
  <ellipse cx="150" cy="260" rx="50" ry="32" fill="#ca8a04"/>
  <ellipse cx="150" cy="256" rx="46" ry="28" fill="#fef08a"/>
  <rect x="120" y="318" width="60" height="22" rx="11" fill="#78350f"/>
  <text x="150" y="333" font-family="'Poppins', sans-serif" font-weight="800" font-size="12" fill="#ffffff" text-anchor="middle">500 g</text>
</svg>"""

with open(os.path.join(output_dir, "haldi-powder.svg"), "w", encoding="utf-8") as f:
    f.write(haldi_svg)

# Food Scroller Images (Section 16: Marquee Banner below Navbar)
marquee_items = [
    ("food-puri-sabji.svg", "#f59e0b", "Crispy Puri & Aloo Dum", "Freshly Cooked"),
    ("food-paneer.svg", "#ef4444", "Shahi Paneer Masala", "Rich & Creamy"),
    ("food-biryani.svg", "#d97706", "Vegetable Dum Biryani", "Aromatic Grains"),
    ("food-dosa.svg", "#ca8a04", "Crispy Masala Dosa", "South Indian Delight"),
    ("food-samosa.svg", "#ea580c", "Golden Desi Samosas", "Evening Crunch"),
    ("food-lassi.svg", "#0284c7", "Kesar Mango Lassi", "Chilled & Refreshing"),
    ("food-salad.svg", "#16a34a", "Organic Sprout Salad", "Nutrient Packed"),
    ("food-gulabjamun.svg", "#b91c1c", "Hot Gulab Jamun", "Pure Desi Ghee"),
]

for filename, color, title, subtitle in marquee_items:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 180" width="280" height="180">
      <defs>
        <linearGradient id="bgGrad_{filename[:4]}" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="{color}"/>
          <stop offset="100%" stop-color="#1e293b"/>
        </linearGradient>
      </defs>
      <rect width="280" height="180" rx="16" fill="url(#bgGrad_{filename[:4]})"/>
      <!-- Decorative circles / food plate simulation -->
      <circle cx="140" cy="80" r="48" fill="rgba(255,255,255,0.15)"/>
      <circle cx="140" cy="80" r="40" fill="#ffffff" opacity="0.95"/>
      <circle cx="140" cy="80" r="34" fill="{color}"/>
      <circle cx="140" cy="80" r="18" fill="#ffffff" opacity="0.8"/>
      <!-- Tag -->
      <rect x="20" y="14" width="90" height="20" rx="10" fill="rgba(0,0,0,0.3)"/>
      <text x="65" y="28" font-family="'Poppins', sans-serif" font-weight="700" font-size="8.5" fill="#ffffff" text-anchor="middle">{subtitle}</text>
      <!-- Title & Union Foods badge -->
      <text x="140" y="145" font-family="'Poppins', sans-serif" font-weight="800" font-size="14" fill="#ffffff" text-anchor="middle">{title}</text>
      <text x="140" y="162" font-family="'Poppins', sans-serif" font-weight="600" font-size="9" fill="#fef08a" text-anchor="middle">Made with 100% Pure Union Foods</text>
    </svg>"""
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(svg)

print("Additional product & marquee banner graphics created!")
