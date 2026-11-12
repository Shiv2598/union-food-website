import shutil, os

# 1. Copy facility image
src_facility = r'C:\Users\ASUS\.gemini\antigravity\brain\04dc5cee-e6bc-4573-8108-f3885bdb5342\.user_uploaded\media_1794482305728.jpg'
dest_facility = r'C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\images\union-foods-facility.jpg'
shutil.copyfile(src_facility, dest_facility)
print('Copied facility image:', dest_facility)

# Also copy as banner-6-harvest.jpg or banner-6-facility.jpg
dest_b6 = r'C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\images\banner-6-harvest.jpg'
shutil.copyfile(src_facility, dest_b6)
print('Updated banner-6-harvest.jpg with genuine facility photo')

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace facility.svg in About section with union-foods-facility.jpg
html = html.replace('assets/images/facility.svg', 'assets/images/union-foods-facility.jpg')

# Remove obsolete inline search script
old_script = '''  <!-- Real-time search script integration -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const searchInput = document.getElementById('quick-search-input');
      const searchResults = document.getElementById('search-results-list');
      if (searchInput && searchResults) {
        searchInput.addEventListener('input', (e) => {
          const q = e.target.value.toLowerCase().trim();
          if (!q) {
            searchResults.innerHTML = '<p style="font-size: 0.85rem; color: var(--text-muted); text-align: center; padding: 1.5rem 0;">Type to see instant search results.</p>';
            return;
          }
          // Query products
          const matches = [
            { name: 'Refined Sunflower Oil (1L)', id: 'uf-oil-1', price: '₹145', cat: 'Cooking Oil', img: 'assets/images/sunflower-oil.svg' },
            { name: 'Premium Sharbati Atta (5Kg)', id: 'uf-atta-1', price: '₹245', cat: 'Flour & Grains', img: 'assets/images/premium-atta.svg' },
            { name: 'Unpolished Moong Dal (1Kg)', id: 'uf-moong-1', price: '₹135', cat: 'Pulses & Dal', img: 'assets/images/moong-dal.svg' },
            { name: 'Desi Chana Dal (1Kg)', id: 'uf-chana-1', price: '₹115', cat: 'Pulses & Dal', img: 'assets/images/chana-dal.svg' },
            { name: 'Kachi Ghani Mustard Oil (1L)', id: 'uf-mustard-1', price: '₹155', cat: 'Cooking Oil', img: 'assets/images/mustard-oil.svg' },
            { name: 'Pure Turmeric Powder (500g)', id: 'uf-haldi-1', price: '₹95', cat: 'Spices', img: 'assets/images/haldi-powder.svg' }
          ].filter(p => p.name.toLowerCase().includes(q) || p.cat.toLowerCase().includes(q));

          if (matches.length === 0) {
            searchResults.innerHTML = '<p style="font-size: 0.85rem; color: #dc2626; text-align: center; padding: 1rem 0;">No matching products found.</p>';
            return;
          }

          searchResults.innerHTML = matches.map(m => `
            <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.6rem 0.8rem; background: var(--bg-warm); border-radius: var(--radius-sm); cursor: pointer;" onclick="window.UnionFoods.openQuickView('${m.id}'); document.getElementById('search-modal').classList.remove('active');">
              <div style="display: flex; align-items: center; gap: 0.65rem;">
                <img src="${m.img}" alt="${m.name}" style="width: 36px; height: 36px; object-fit: contain;">
                <div>
                  <div style="font-size: 0.88rem; font-weight: 700; color: var(--text-heading);">${m.name}</div>
                  <span style="font-size: 0.75rem; color: var(--text-muted);">${m.cat}</span>
                </div>
              </div>
              <strong style="color: var(--primary-orange);">${m.price}</strong>
            </div>
          `).join('');
        });
      }
    });
  </script>'''

if old_script in html:
    html = html.replace(old_script, '')
    print('Removed obsolete inline search script')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html successfully!')
