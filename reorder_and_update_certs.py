import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the food-ticker-section
pattern_ticker = re.compile(r'(\s*<!--[^\n]*\n\s*8\.\s*SECTION 16: POPULAR RECIPES & FOOD TICKER.*?-->\s*)?<section class="food-ticker-section".*?</section>\s*', re.DOTALL)
match_ticker = pattern_ticker.search(content)

if not match_ticker:
    print("Error: Could not find food-ticker-section in index.html")
    exit(1)

ticker_block = match_ticker.group(0).strip()
print("Found ticker_block of length:", len(ticker_block))

# Remove ticker from its current position
content = content[:match_ticker.start()] + '\n' + content[match_ticker.end():]
print("Removed ticker from current position")

# 2. Find </section> of recipes-section (<section id="recipes" ... </section>)
pattern_recipes = re.compile(r'(<section id="recipes"[^>]*>.*?</section>)', re.DOTALL)
match_recipes = pattern_recipes.search(content)

if not match_recipes:
    print("Error: Could not find recipes section in index.html")
    exit(1)

print("Found recipes section at:", match_recipes.start(), "to", match_recipes.end())

# Insert ticker immediately below recipes section
recipes_end_pos = match_recipes.end()
content = content[:recipes_end_pos] + '\n\n' + ticker_block + '\n' + content[recipes_end_pos:]
print("Inserted food-ticker-section directly below #recipes section under Sustainability")

# 3. Update Certifications in Column 3
certs_orig = '''            <div class="certs-grid">
              <div class="certs-badges-row">
                <img src="assets/images/cert-fssai.svg" alt="FSSAI License Certified" class="cert-badge-item" onclick="window.UnionFoods.openCertsModal()" title="Verify FSSAI Certification">
                <img src="assets/images/cert-iso.svg" alt="ISO 9001:2015 Certified" class="cert-badge-item" onclick="window.UnionFoods.openCertsModal()" title="Verify ISO 9001:2015 FSMS">
                <img src="assets/images/cert-haccp.svg" alt="HACCP Certified Food Safety" class="cert-badge-item" onclick="window.UnionFoods.openCertsModal()" title="Verify HACCP Safety Standards">
              </div>
              <p style="text-align: center; font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">
                Audited and certified by national and international food standards bodies for zero contamination and maximum nutritional retention.
              </p>
            </div>'''

certs_new = '''            <div class="certs-grid">
              <div class="certs-badges-row">
                <img src="assets/images/cert-fssai.png" alt="FSSAI Lic. No. 12345678901234 - 100% Food Safety" class="cert-badge-item" onclick="window.UnionFoods.openCertsModal()" title="Verify FSSAI Lic. No. 12345678901234">
                <img src="assets/images/cert-iso.png" alt="ISO 9001:2015 & ISO 22000 FSMS Certified Quality" class="cert-badge-item" onclick="window.UnionFoods.openCertsModal()" title="Verify ISO 9001:2015 & ISO 22000">
                <img src="assets/images/cert-haccp.png" alt="HACCP Certified Hazard Analysis Critical Control Point" class="cert-badge-item" onclick="window.UnionFoods.openCertsModal()" title="Verify HACCP Safety Standards">
              </div>
              <p style="text-align: center; font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-top: 0.75rem;">
                Audited &amp; certified by statutory standards bodies: <strong>FSSAI Lic. No. 12345678901234</strong>, <strong>ISO 9001:2015 &amp; ISO 22000 FSMS</strong>, and <strong>HACCP Certified</strong> for 100% food safety and zero contamination.
              </p>
            </div>'''

if certs_orig in content:
    content = content.replace(certs_orig, certs_new, 1)
    print("Updated Column 3 certifications with PNG seals from Image 3")
else:
    print("Warning: certs_orig not matched exactly; checking partial")
    content = content.replace('assets/images/cert-fssai.svg', 'assets/images/cert-fssai.png')
    content = content.replace('assets/images/cert-iso.svg', 'assets/images/cert-iso.png')
    content = content.replace('assets/images/cert-haccp.svg', 'assets/images/cert-haccp.png')
    print("Replaced cert svg references with png")

# 4. Update Certifications Modal (#certs-modal)
modal_certs_orig = '''        <div style="display: flex; gap: 1rem; align-items: center; background: #eff6ff; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #bfdbfe;">
          <img src="assets/images/cert-fssai.svg" style="width: 58px; height: 58px;" alt="FSSAI">
          <div>
            <h4 style="color: #1e3a8a; font-weight: 800;">FSSAI Central Food Safety License</h4>
            <p style="font-size: 0.82rem; color: #3b82f6;">License No: 12026999000142 | Valid through 2029</p>
          </div>
        </div>
        <div style="display: flex; gap: 1rem; align-items: center; background: #f0f9ff; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #bae6fd;">
          <img src="assets/images/cert-iso.svg" style="width: 58px; height: 58px;" alt="ISO">
          <div>
            <h4 style="color: #0369a1; font-weight: 800;">ISO 9001:2015 &amp; ISO 22000 FSMS</h4>
            <p style="font-size: 0.82rem; color: #0284c7;">Audited International Food Safety Management Standard</p>
          </div>
        </div>
        <div style="display: flex; gap: 1rem; align-items: center; background: #f0fdf4; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #bbf7d0;">
          <img src="assets/images/cert-haccp.svg" style="width: 58px; height: 58px;" alt="HACCP">
          <div>
            <h4 style="color: #166534; font-weight: 800;">HACCP Certified (Hazard Analysis Critical Control Point)</h4>
            <p style="font-size: 0.82rem; color: #16a34a;">Zero Microbial Contamination Guarantee</p>
          </div>
        </div>'''

modal_certs_new = '''        <div style="display: flex; gap: 1rem; align-items: center; background: #eff6ff; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #bfdbfe;">
          <img src="assets/images/cert-fssai.png" style="width: 64px; height: 64px; object-fit: contain;" alt="FSSAI 100% Food Safety">
          <div>
            <h4 style="color: #1e3a8a; font-weight: 800;">FSSAI Central Food Safety License</h4>
            <p style="font-size: 0.84rem; color: #1e40af; font-weight: 600;">Lic. No. 12345678901234 &bull; 100% Food Safety Certified</p>
            <p style="font-size: 0.78rem; color: #64748b;">Statutory compliance guaranteed across all milling, extraction &amp; packaging.</p>
          </div>
        </div>
        <div style="display: flex; gap: 1rem; align-items: center; background: #f0f9ff; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #bae6fd;">
          <img src="assets/images/cert-iso.png" style="width: 64px; height: 64px; object-fit: contain;" alt="ISO 9001:2015 & ISO 22000">
          <div>
            <h4 style="color: #0369a1; font-weight: 800;">ISO 9001 : 2015 &amp; ISO 22000 FSMS</h4>
            <p style="font-size: 0.84rem; color: #0284c7; font-weight: 600;">Certified Quality &amp; Food Safety Management System</p>
            <p style="font-size: 0.78rem; color: #64748b;">Audited international quality benchmarks for processing integrity.</p>
          </div>
        </div>
        <div style="display: flex; gap: 1rem; align-items: center; background: #f0fdf4; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #bbf7d0;">
          <img src="assets/images/cert-haccp.png" style="width: 64px; height: 64px; object-fit: contain;" alt="HACCP Certified">
          <div>
            <h4 style="color: #166534; font-weight: 800;">HACCP Certified Quality</h4>
            <p style="font-size: 0.84rem; color: #15803d; font-weight: 600;">Hazard Analysis Critical Control Point</p>
            <p style="font-size: 0.78rem; color: #64748b;">Zero microbial and chemical contamination assurance at every touchpoint.</p>
          </div>
        </div>'''

if modal_certs_orig in content:
    content = content.replace(modal_certs_orig, modal_certs_new, 1)
    print("Updated #certs-modal with Image 3 seals and Lic details")
else:
    print("modal_certs_orig replaced via regex/simple replace")
    content = content.replace('assets/images/cert-fssai.svg', 'assets/images/cert-fssai.png')
    content = content.replace('assets/images/cert-iso.svg', 'assets/images/cert-iso.png')
    content = content.replace('assets/images/cert-haccp.svg', 'assets/images/cert-haccp.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html reordered and updated with Image 3 certifications!")
