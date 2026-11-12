import re

with open('index.html.bak', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update <head> with Favicon links
head_orig = '  <!-- Primary CSS Stylesheet -->'
head_new = '''  <!-- Favicon & Touch Icons -->
  <link rel="icon" type="image/png" sizes="128x128" href="assets/images/favicon.png">
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="assets/images/favicon.png">

  <!-- Primary CSS Stylesheet -->'''

if head_orig in content:
    content = content.replace(head_orig, head_new, 1)
    print("1. Favicons added to <head>")
else:
    print("Warning: head_orig not found")

# 2. Remove top-bar (<aside class="top-bar"> ... </aside>)
# Regex to match from comment or <aside class="top-bar" up to </aside>
pattern_topbar = re.compile(r'(\s*<!--[^\n]*\n\s*1\.\s*TOP UTILITY BAR.*?-->\s*)?<aside class="top-bar".*?</aside>\s*', re.DOTALL)
content, count = pattern_topbar.subn('\n', content, count=1)
print(f"2. Top bar removed: {count} matches")

# 3. Update Brand Logo in Header
content = content.replace(
    '<img src="assets/images/logo.svg" alt="Union Foods Logo" class="brand-logo-img">',
    '<img src="assets/images/union-foods-logo.png" alt="Union Foods - Crafting Quality Est. 1982" class="brand-logo-img">'
)
print("3. Header logo updated to union-foods-logo.png")

# 4. Add Smart Search Input in Header Navigation & update Header Actions
header_actions_orig = '''      <!-- Header Actions -->
      <div class="header-actions">
        <!-- Search Trigger -->
        <button class="action-icon-btn" onclick="document.getElementById('search-modal').classList.add('active')" title="Search Food Items" aria-label="Search">
          <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
        </button>'''

header_actions_new = '''      <!-- Smart Search Input in Header (Desktop / Tablet) -->
      <div class="header-search-wrap" id="header-search-wrap">
        <form class="header-search-form" onsubmit="window.UnionFoods.handleHeaderSearch(event)">
          <div class="search-input-shell">
            <span class="search-prefix-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
            </span>
            <input 
              type="search" 
              id="nav-search-input" 
              class="nav-search-input" 
              placeholder="Search products, categories, offers..." 
              autocomplete="off" 
              aria-label="Search Union Foods website content"
              aria-autocomplete="list"
              aria-controls="nav-search-suggestions"
            >
            <button type="button" id="nav-search-clear-btn" class="nav-search-clear-btn" aria-label="Clear search query" style="display: none;">
              <svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
            </button>
            <button type="submit" class="nav-search-submit-btn" aria-label="Submit search">
              <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
            </button>
          </div>
        </form>

        <!-- Live Autocomplete Suggestions Dropdown -->
        <div id="nav-search-suggestions" class="nav-search-suggestions" role="listbox" aria-label="Search suggestions" style="display: none;">
          <div class="suggestions-header">Quick Matches</div>
          <div id="suggestions-list-box" class="suggestions-list-box"></div>
          <div class="suggestions-footer">
            <span>Press <kbd>&uarr;</kbd> <kbd>&darr;</kbd> to navigate, <kbd>&crarr;</kbd> to select, <kbd>Esc</kbd> to close</span>
          </div>
        </div>
      </div>

      <!-- Header Actions -->
      <div class="header-actions">
        <!-- Search Trigger (Modal for Mobile & Quick View) -->
        <button class="action-icon-btn mobile-search-btn" onclick="window.UnionFoods.openSearchModal()" title="Search Food Items" aria-label="Search">
          <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
        </button>

        <!-- Header Theme Toggle -->
        <button id="theme-toggle-btn" class="action-icon-btn" title="Toggle Light/Dark Theme" aria-label="Toggle Theme">
          <svg viewBox="0 0 24 24"><path d="M12 3a9 9 0 1 0 9 9c0-.46-.04-.92-.1-1.36a5.389 5.389 0 0 1-4.4 2.26 5.403 5.403 0 0 1-3.14-9.8c-.44-.06-.9-.1-1.36-.1z"/></svg>
        </button>'''

if header_actions_orig in content:
    content = content.replace(header_actions_orig, header_actions_new, 1)
    print("4. Header search bar and actions updated")
else:
    print("Warning: header_actions_orig not matched")

# 5. Replace Old Food Ticker below navbar with the New Hero 6-Image Slider
pattern_ticker_old = re.compile(r'(\s*<!--[^\n]*\n\s*3\.\s*SECTION 16: INFINITE SCROLLING FOOD IMAGE GALLERY.*?-->\s*)?<section class="food-ticker-section".*?</section>\s*', re.DOTALL)

hero_slider_code = '''
  <!-- ==========================================================================
       3. BELOW-NAVBAR HERO IMAGE SLIDER (5/6 Auto-Scrolling Images)
       ========================================================================== -->
  <section id="hero-slider" class="hero-slider-section" aria-label="Union Foods Featured Visual Highlights">
    <div class="hero-slider-container">
      <div class="hero-slider-track" id="hero-slider-track">
        <!-- Slide 1: Panoramic Product Showcase -->
        <div class="hero-slide active" data-index="0">
          <img src="assets/images/banner-1-products.jpg" alt="Union Foods Quality Crafting Range" class="hero-slide-img" loading="eager">
          <div class="hero-slide-overlay">
            <div class="container slide-content-box">
              <span class="slide-tag">Pure Food For A Healthier Life</span>
              <h2 class="slide-heading">Crafting Purity &amp; Quality Since 1982</h2>
              <p class="slide-desc">From whole farm-fresh grains to 100% natural cold-pressed oils, experience nutrition without compromise.</p>
              <div class="slide-cta-row">
                <a href="#products-section" class="btn-primary">Explore Products &rarr;</a>
                <button class="btn-secondary" onclick="window.UnionFoods.openSearchModal('Offers')">Limited Offers</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Slide 2: Golden Wheat Harvest & Farmer -->
        <div class="hero-slide" data-index="1">
          <img src="assets/images/banner-2-farmer.jpg" alt="Odisha Golden Wheat Fields &amp; Farming Tradition" class="hero-slide-img" loading="lazy">
          <div class="hero-slide-overlay">
            <div class="container slide-content-box">
              <span class="slide-tag">Farm-Direct Purity</span>
              <h2 class="slide-heading">Sourced Direct From Trusted Indian Farmers</h2>
              <p class="slide-desc">Grounded in traditional cultivation, supporting local farm communities across Odisha with fair trade practices.</p>
              <div class="slide-cta-row">
                <a href="#why-choose" class="btn-primary">Our Farm Promise &rarr;</a>
                <a href="#locations" class="btn-secondary">Explore Locations</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Slide 3: Authentic Indian Culinary Delights -->
        <div class="hero-slide" data-index="2">
          <img src="assets/images/banner-3-culinary.jpg" alt="Authentic Culinary Delights" class="hero-slide-img" loading="lazy">
          <div class="hero-slide-overlay">
            <div class="container slide-content-box">
              <span class="slide-tag">Master Chef Recipes</span>
              <h2 class="slide-heading">Master Every Recipe With Pure Staples</h2>
              <p class="slide-desc">From steaming Shahi Paneer to crispy rotis, golden samosas and dal fry, taste purity in every home recipe.</p>
              <div class="slide-cta-row">
                <a href="#recipes" class="btn-primary">Explore Recipes &rarr;</a>
                <button class="btn-secondary" onclick="window.UnionFoods.openRecipeModal()">Cook Tonight</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Slide 4: Complete Pantry Family Packaging -->
        <div class="hero-slide" data-index="3">
          <img src="assets/images/banner-4-pantry.jpg" alt="Union Foods Complete Grocery Pantry Collection" class="hero-slide-img" loading="lazy">
          <div class="hero-slide-overlay">
            <div class="container slide-content-box">
              <span class="slide-tag">Complete Daily Essentials</span>
              <h2 class="slide-heading">Oils, Atta, Dals, Spices &amp; Snacks</h2>
              <p class="slide-desc">Triple-cleaned, micro-filtered, and sealed with tamper-evident hygienic packaging for guaranteed freshness.</p>
              <div class="slide-cta-row">
                <a href="#products-section" class="btn-primary">Shop All Essentials &rarr;</a>
                <button class="btn-secondary" onclick="window.UnionFoods.openCartDrawer()">Fast Order</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Slide 5: The 6 Product Categories Emblem -->
        <div class="hero-slide" data-index="4">
          <img src="assets/images/banner-5-categories.jpg" alt="Union Foods 6 Core Categories" class="hero-slide-img" loading="lazy">
          <div class="hero-slide-overlay">
            <div class="container slide-content-box">
              <span class="slide-tag">Certified Nutrition</span>
              <h2 class="slide-heading">FSSAI Certified &amp; ISO 22000 Approved</h2>
              <p class="slide-desc">Six core nutritional categories developed to safeguard the health, energy, and wellness of your family.</p>
              <div class="slide-cta-row">
                <a href="#categories-section" class="btn-primary">Browse Categories &rarr;</a>
                <a href="#certifications-section" class="btn-secondary">View Quality Certs</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Slide 6: Express Delivery Harvest Banner -->
        <div class="hero-slide" data-index="5">
          <img src="assets/images/banner-6-harvest.jpg" alt="Golden Harvest Odisha" class="hero-slide-img" loading="lazy">
          <div class="hero-slide-overlay">
            <div class="container slide-content-box">
              <span class="slide-tag">Express Delivery In Odisha</span>
              <h2 class="slide-heading">Delivering Farm Purity Straight To Your Door</h2>
              <p class="slide-desc">Enjoy free same-day or next-day express delivery across Bhubaneswar, Cuttack, and Odisha on orders above ₹499.</p>
              <div class="slide-cta-row">
                <button class="btn-primary" onclick="window.UnionFoods.startCheckout()">Order Online Now &rarr;</button>
                <a href="#locations" class="btn-secondary">Check PIN Code</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Slider Controls -->
      <button id="hero-slider-prev" class="slider-arrow-btn prev" aria-label="Previous Slide">
        <svg viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
      </button>
      <button id="hero-slider-next" class="slider-arrow-btn next" aria-label="Next Slide">
        <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      </button>

      <!-- Slide Indicators -->
      <div class="slider-dots" id="hero-slider-dots">
        <button class="slider-dot active" data-index="0" aria-label="Slide 1"></button>
        <button class="slider-dot" data-index="1" aria-label="Slide 2"></button>
        <button class="slider-dot" data-index="2" aria-label="Slide 3"></button>
        <button class="slider-dot" data-index="3" aria-label="Slide 4"></button>
        <button class="slider-dot" data-index="4" aria-label="Slide 5"></button>
        <button class="slider-dot" data-index="5" aria-label="Slide 6"></button>
      </div>
    </div>
  </section>
'''

content, count_ticker = pattern_ticker_old.subn(hero_slider_code, content, count=1)
print(f"5. Old ticker replaced with Hero 6-image slider: {count_ticker} matches")

# 6. Insert Shifted Food Ticker immediately below Section 17 (offers-slider-section)
shifted_food_ticker = '''
    <!-- ==========================================================================
         8. SECTION 16: POPULAR RECIPES & FOOD TICKER (Shifted Below Limited Deals)
         ========================================================================== -->
    <section class="food-ticker-section" aria-label="Popular Dishes & Delicacies Made with Union Foods">
      <div class="container" style="padding-top: 1.5rem; padding-bottom: 0.75rem;">
        <div class="section-title-wrap">
          <span class="section-tag">Chef's Recommendations</span>
          <h2 class="section-title" style="font-size: clamp(1.4rem, 2.2vw, 2rem); margin-bottom: 0.35rem;">Popular Dishes Prepared with Union Foods Staples</h2>
          <p style="font-size: 0.9rem; color: var(--text-muted); max-width: 680px;">Taste authentic Indian culinary perfection. Click on any dish below to view the recipe ingredients, step-by-step instructions, and scale servings!</p>
        </div>
      </div>
      <div class="ticker-wrapper">
        <div class="ticker-track">
          <!-- Loop Item 1 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('puri-sabji')">
            <img src="assets/images/food-puri-sabji.jpg" alt="Crispy Puri & Aloo Dum" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">Breakfast Favorite</span>
              <span class="ticker-name">Crispy Puri &amp; Aloo Dum</span>
            </div>
          </div>
          <!-- Loop Item 2 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('shahi-paneer')">
            <img src="assets/images/food-paneer.jpg" alt="Shahi Paneer Masala" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">Rich &amp; Creamy</span>
              <span class="ticker-name">Shahi Paneer Masala</span>
            </div>
          </div>
          <!-- Loop Item 3 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('biryani')">
            <img src="assets/images/food-biryani.jpg" alt="Vegetable Dum Biryani" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">Special Weekend Dish</span>
              <span class="ticker-name">Vegetable Dum Biryani</span>
            </div>
          </div>
          <!-- Loop Item 4 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('dosa')">
            <img src="assets/images/food-dosa.jpg" alt="Crispy Masala Dosa" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">South Indian Crunch</span>
              <span class="ticker-name">Crispy Masala Dosa</span>
            </div>
          </div>
          <!-- Loop Item 5 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('samosa')">
            <img src="assets/images/food-samosa.jpg" alt="Golden Desi Samosas" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">Evening Snack</span>
              <span class="ticker-name">Golden Desi Samosas</span>
            </div>
          </div>
          <!-- Loop Item 6 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('lassi')">
            <img src="assets/images/food-lassi.jpg" alt="Kesar Mango Lassi" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">Refreshing Beverage</span>
              <span class="ticker-name">Kesar Mango Lassi</span>
            </div>
          </div>
          <!-- Loop Item 7 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('salad')">
            <img src="assets/images/food-salad.jpg" alt="Organic Sprout Salad" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">Health &amp; Fitness</span>
              <span class="ticker-name">Organic Sprout Salad</span>
            </div>
          </div>
          <!-- Loop Item 8 -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('gulab-jamun')">
            <img src="assets/images/food-gulabjamun.jpg" alt="Hot Gulab Jamun" loading="lazy">
            <div class="ticker-overlay">
              <span class="ticker-tag">Desi Ghee Dessert</span>
              <span class="ticker-name">Hot Gulab Jamun</span>
            </div>
          </div>

          <!-- Seamless duplicate for smooth infinite loop -->
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('puri-sabji')">
            <img src="assets/images/food-puri-sabji.jpg" alt="Crispy Puri & Aloo Dum" loading="lazy">
            <div class="ticker-overlay"><span class="ticker-tag">Breakfast Favorite</span><span class="ticker-name">Crispy Puri &amp; Aloo Dum</span></div>
          </div>
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('shahi-paneer')">
            <img src="assets/images/food-paneer.jpg" alt="Shahi Paneer Masala" loading="lazy">
            <div class="ticker-overlay"><span class="ticker-tag">Rich &amp; Creamy</span><span class="ticker-name">Shahi Paneer Masala</span></div>
          </div>
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('biryani')">
            <img src="assets/images/food-biryani.jpg" alt="Vegetable Dum Biryani" loading="lazy">
            <div class="ticker-overlay"><span class="ticker-tag">Special Weekend Dish</span><span class="ticker-name">Vegetable Dum Biryani</span></div>
          </div>
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('dosa')">
            <img src="assets/images/food-dosa.jpg" alt="Crispy Masala Dosa" loading="lazy">
            <div class="ticker-overlay"><span class="ticker-tag">South Indian Crunch</span><span class="ticker-name">Crispy Masala Dosa</span></div>
          </div>
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('samosa')">
            <img src="assets/images/food-samosa.jpg" alt="Golden Desi Samosas" loading="lazy">
            <div class="ticker-overlay"><span class="ticker-tag">Evening Snack</span><span class="ticker-name">Golden Desi Samosas</span></div>
          </div>
          <div class="ticker-card" onclick="window.UnionFoods.openRecipeModal('lassi')">
            <img src="assets/images/food-lassi.jpg" alt="Kesar Mango Lassi" loading="lazy">
            <div class="ticker-overlay"><span class="ticker-tag">Refreshing Beverage</span><span class="ticker-name">Kesar Mango Lassi</span></div>
          </div>
        </div>
      </div>
    </section>
'''

offers_end = '</section>\n\n    <!-- ==========================================================================\n         7. OUR PRODUCT CATEGORIES'
if offers_end in content:
    content = content.replace(offers_end, '</section>\n' + shifted_food_ticker + '\n    <!-- ==========================================================================\n         7. OUR PRODUCT CATEGORIES', 1)
    print("6. Shifted Food Ticker inserted below Limited Period Deals")
else:
    print("Warning: offers_end exact match not found; trying regex")
    content = re.sub(r'(<section class="offers-slider-section".*?</section>)(\s*<!--[^\n]*\n\s*7\.\s*OUR PRODUCT CATEGORIES)', r'\1\n' + shifted_food_ticker + r'\2', content, flags=re.DOTALL)
    print("6. Shifted Food Ticker inserted via regex")

# 7. Update Categories with extracted genuine category cards
categories_orig = '''        <div class="categories-grid">
          <!-- 1. Cooking Oil -->
          <div class="category-card" data-cat="oil" title="View Cooking Oils">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-cooking-oil.svg" alt="Cooking Oil">
            </div>
            <span class="category-name">Cooking Oil</span>
          </div>

          <!-- 2. Flour & Grains -->
          <div class="category-card" data-cat="flour" title="View Flour & Grains">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-flour-grains.svg" alt="Flour & Grains">
            </div>
            <span class="category-name">Flour & Grains</span>
          </div>

          <!-- 3. Pulses & Dal -->
          <div class="category-card" data-cat="pulses" title="View Pulses & Dal">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-pulses-dal.svg" alt="Pulses & Dal">
            </div>
            <span class="category-name">Pulses & Dal</span>
          </div>

          <!-- 4. Spices -->
          <div class="category-card" data-cat="spices" title="View Spices">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-spices.svg" alt="Pure Spices">
            </div>
            <span class="category-name">Spices</span>
          </div>

          <!-- 5. Snacks -->
          <div class="category-card" data-cat="snacks" title="View Snacks">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-snacks.svg" alt="Healthy Snacks">
            </div>
            <span class="category-name">Snacks</span>
          </div>

          <!-- 6. Beverages -->
          <div class="category-card" data-cat="beverages" title="View Beverages">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-beverages.svg" alt="Beverages">
            </div>
            <span class="category-name">Beverages</span>
          </div>

          <!-- 7. Packaged Foods -->
          <div class="category-card" data-cat="packaged" title="View Packaged Foods">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-packaged-foods.svg" alt="Packaged Foods">
            </div>
            <span class="category-name">Packaged Foods</span>
          </div>
        </div>'''

categories_new = '''        <div class="categories-grid">
          <!-- 1. Cooking Oil -->
          <div class="category-card" data-cat="oil" title="View Cooking Oils">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-oil.jpg" alt="Union Foods Cooking Oil" loading="lazy">
            </div>
            <span class="category-name">Cooking Oil</span>
          </div>

          <!-- 2. Flour & Grains -->
          <div class="category-card" data-cat="flour" title="View Flour & Grains">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-flour.jpg" alt="Union Foods Flour & Grains" loading="lazy">
            </div>
            <span class="category-name">Flour & Grains</span>
          </div>

          <!-- 3. Pulses & Dal -->
          <div class="category-card" data-cat="pulses" title="View Pulses & Dal">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-pulses.jpg" alt="Union Foods Pulses & Dal" loading="lazy">
            </div>
            <span class="category-name">Pulses & Dal</span>
          </div>

          <!-- 4. Spices -->
          <div class="category-card" data-cat="spices" title="View Spices">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-spices.jpg" alt="Union Foods Pure Spices" loading="lazy">
            </div>
            <span class="category-name">Spices</span>
          </div>

          <!-- 5. Snacks -->
          <div class="category-card" data-cat="snacks" title="View Snacks">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-snacks.jpg" alt="Union Foods Healthy Snacks" loading="lazy">
            </div>
            <span class="category-name">Snacks</span>
          </div>

          <!-- 6. Beverages -->
          <div class="category-card" data-cat="beverages" title="View Beverages">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-beverages.jpg" alt="Union Foods Pure Beverages" loading="lazy">
            </div>
            <span class="category-name">Beverages</span>
          </div>

          <!-- 7. Packaged Foods -->
          <div class="category-card" data-cat="packaged" title="View Packaged Foods">
            <div class="category-icon-wrap">
              <img src="assets/images/cat-packaged-foods.svg" alt="Packaged Foods" loading="lazy">
            </div>
            <span class="category-name">Packaged Foods</span>
          </div>
        </div>'''

if categories_orig in content:
    content = content.replace(categories_orig, categories_new, 1)
    print("7. Categories updated with genuine Union Foods cards")
else:
    print("Warning: categories_orig not matched")

# 8. Update Footer Logo
footer_logo_orig = '<img src="assets/images/logo-white.svg" alt="Union Foods White Logo" style="height: 44px;">'
footer_logo_new = '<img src="assets/images/union-foods-logo-white.png" alt="Union Foods - Crafting Quality Est. 1982" class="footer-logo-img">'
if footer_logo_orig in content:
    content = content.replace(footer_logo_orig, footer_logo_new, 1)
    print("8. Footer logo updated to union-foods-logo-white.png")
else:
    print("Warning: footer_logo_orig not matched")

# 9. Replace old Search Modal with Comprehensive Smart Search Engine Dashboard
pattern_search_modal = re.compile(r'<!-- Search Modal -->\s*<div id="search-modal".*?</div>\s*</div>\s*', re.DOTALL)

smart_search_modal_code = '''  <!-- ==========================================================================
       SMART SEARCH MODAL & RESULTS DASHBOARD (Site-Wide Engine)
       ========================================================================== -->
  <div id="search-modal" class="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="search-modal-title">
    <div class="modal-content-box search-modal-box">
      <button class="modal-close-btn" onclick="window.UnionFoods.closeSearchModal()" aria-label="Close search dialog">
        <svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
      </button>

      <!-- Search Header -->
      <div class="search-modal-header">
        <div class="search-title-row">
          <img src="assets/images/union-foods-logo.png" alt="Union Foods" class="search-brand-mark">
          <h2 id="search-modal-title" class="search-modal-heading">Smart Search Engine</h2>
        </div>
        <p class="search-modal-sub">Search across all products, cooking oils, grains, dals, spices, offers, recipes, certifications &amp; company information.</p>
        
        <!-- Search Input Bar with Clear & Submit -->
        <div class="search-bar-composite">
          <span class="search-composite-icon">
            <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
          </span>
          <input 
            type="search" 
            id="modal-search-input" 
            class="modal-search-input" 
            placeholder="Search products, categories, offers, recipes..." 
            autocomplete="off" 
            aria-label="Search website"
          >
          <button type="button" id="modal-search-clear" class="search-clear-btn" aria-label="Clear search text" style="display: none;">
            <svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
          </button>
        </div>

        <!-- Filter Pills -->
        <div class="search-filter-pills" id="search-filter-pills" role="tablist" aria-label="Filter search results by type">
          <button type="button" class="search-filter-pill active" data-filter="all">All Content (<span id="count-all">0</span>)</button>
          <button type="button" class="search-filter-pill" data-filter="product">Products (<span id="count-product">0</span>)</button>
          <button type="button" class="search-filter-pill" data-filter="category">Categories (<span id="count-category">0</span>)</button>
          <button type="button" class="search-filter-pill" data-filter="offer">Offers &amp; Deals (<span id="count-offer">0</span>)</button>
          <button type="button" class="search-filter-pill" data-filter="recipe">Recipes (<span id="count-recipe">0</span>)</button>
          <button type="button" class="search-filter-pill" data-filter="info">Company Info (<span id="count-info">0</span>)</button>
          <button type="button" class="search-filter-pill" data-filter="certification">Certifications (<span id="count-certification">0</span>)</button>
        </div>

        <!-- Sort & Controls Row -->
        <div class="search-toolbar">
          <div class="search-status-text" id="search-status-text">Showing popular recommendations</div>
          <div class="search-sort-wrap">
            <label for="search-sort-select">Sort by:</label>
            <select id="search-sort-select" class="search-sort-select" onchange="window.UnionFoods.triggerSearchReSort()">
              <option value="relevance">Best Match</option>
              <option value="price-asc">Price: Low to High</option>
              <option value="price-desc">Price: High to Low</option>
              <option value="name-asc">Name: A to Z</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Search Body -->
      <div class="search-modal-body">
        <!-- Recent & Popular Search Chips -->
        <div id="search-defaults-box" class="search-defaults-box">
          <div class="search-chips-block" id="recent-searches-block" style="display: none;">
            <div class="search-chips-header">
              <span>Recent Searches</span>
              <button type="button" class="clear-history-btn" onclick="window.UnionFoods.clearSearchHistory()">Clear History</button>
            </div>
            <div id="recent-chips-container" class="search-chips-list"></div>
          </div>

          <div class="search-chips-block">
            <div class="search-chips-header">
              <span>Popular Searches</span>
            </div>
            <div class="search-chips-list">
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('Mustard Oil')">Mustard Oil</button>
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('Sharbati Atta')">Sharbati Atta</button>
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('Moong Dal')">Moong Dal</button>
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('Sunflower Oil')">Sunflower Oil</button>
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('Turmeric Spices')">Pure Turmeric</button>
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('BOGO Offer')">BOGO Free Offer</button>
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('FSSAI Certification')">FSSAI Certification</button>
              <button type="button" class="search-chip" onclick="window.UnionFoods.applySearchChip('Bhubaneswar Hub')">Bhubaneswar Hub</button>
            </div>
          </div>
        </div>

        <!-- Search Results Grid (Responsive: 4 cols desktop, 2-3 cols tablet, 1-2 cols mobile) -->
        <div id="search-results-grid" class="search-results-grid"></div>

        <!-- No Results Fallback -->
        <div id="search-no-results" class="search-no-results" style="display: none;">
          <div class="no-results-icon">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="var(--text-muted)"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
          </div>
          <h3>Sorry! We couldn't find what you're looking for.</h3>
          <p>Please double-check your spelling or explore these popular categories:</p>
          <div class="no-results-quick-links">
            <button type="button" class="btn-sm-tag" onclick="window.UnionFoods.applySearchChip('Cooking Oil')">Cooking Oil</button>
            <button type="button" class="btn-sm-tag" onclick="window.UnionFoods.applySearchChip('Flour')">Chakki Atta</button>
            <button type="button" class="btn-sm-tag" onclick="window.UnionFoods.applySearchChip('Pulses')">Organic Dals</button>
            <button type="button" class="btn-sm-tag" onclick="window.UnionFoods.applySearchChip('Spices')">Pure Spices</button>
          </div>
          <button type="button" class="btn-primary" style="margin-top: 1rem;" onclick="window.UnionFoods.closeSearchModal(); window.location.href='#home';">
            Return to Homepage
          </button>
        </div>
      </div>
    </div>
  </div>
'''

content, count_modal = pattern_search_modal.subn(smart_search_modal_code, content, count=1)
print(f"9. Search modal updated: {count_modal} matches")

# 10. Clean up old inline quick-search listener at bottom of index.html
inline_search_pattern = re.compile(r'// Live quick search.*?\}\);\s*\}\s*\}\);\s*</script>', re.DOTALL)
content = inline_search_pattern.sub('  });\n  </script>', content)
print("10. Cleaned up old inline search listener in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated!")
