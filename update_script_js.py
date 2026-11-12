with open('js/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Let's check where to inject the search engine and slider controller.
# It can be placed right before the window.UnionFoods export, and exposed on window.UnionFoods!

search_and_slider_code = '''
  /* ==========================================================================
     SMART SEARCH ENGINE KNOWLEDGE BASE (18 Comprehensive Content Domains)
     ========================================================================== */
  const SEARCH_DATABASE = [
    // 1. Products - Cooking Oils
    {
      id: 'search-oil-1',
      name: 'Refined Sunflower Oil (1L & 5L)',
      category: 'Cooking Oil',
      type: 'product',
      price: 145,
      priceDisplay: '₹145',
      image: 'assets/images/sunflower-oil.svg',
      description: 'Triple refined, 100% pure sunflower oil enriched with Vitamins A & D. Light, healthy, and cholesterol-free for everyday family cooking.',
      keywords: ['oil', 'sunflower', 'cooking oil', 'refined oil', 'heart healthy', 'fry', 'kitchen staples'],
      url: '#products-section',
      actionId: 'uf-oil-1'
    },
    {
      id: 'search-oil-2',
      name: 'Kachi Ghani Mustard Oil (1L)',
      category: 'Cooking Oil',
      type: 'product',
      price: 155,
      priceDisplay: '₹155',
      image: 'assets/images/mustard-oil.svg',
      description: 'Cold-pressed traditional mustard oil with strong pungency and natural antioxidants. Ideal for authentic pickles and pungent curries.',
      keywords: ['oil', 'mustard oil', 'kachi ghani', 'sarson tel', 'pungent', 'pickles', 'traditional'],
      url: '#products-section',
      actionId: 'uf-mustard-1'
    },

    // 2. Products - Flour & Grains
    {
      id: 'search-atta-1',
      name: 'Premium Sharbati Atta (5Kg & 10Kg)',
      category: 'Flour & Grains',
      type: 'product',
      price: 245,
      priceDisplay: '₹245',
      image: 'assets/images/premium-atta.svg',
      description: '100% whole wheat chakki fresh flour milled from golden Sharbati grains. Makes rotis that stay soft, fluffy, and aromatic for hours.',
      keywords: ['atta', 'wheat', 'flour', 'sharbati', 'chakki fresh', 'roti', 'chapati', 'whole wheat', 'grains'],
      url: '#products-section',
      actionId: 'uf-atta-1'
    },

    // 3. Products - Pulses & Dal
    {
      id: 'search-dal-1',
      name: 'Unpolished Moong Dal (1Kg)',
      category: 'Pulses & Dal',
      type: 'product',
      price: 135,
      priceDisplay: '₹135',
      image: 'assets/images/moong-dal.svg',
      description: 'Premium unpolished yellow moong lentils with natural nutrients and wholesome flavor intact. Easy to digest and rich in plant protein.',
      keywords: ['dal', 'moong dal', 'pulses', 'lentils', 'yellow dal', 'protein', 'unpolished'],
      url: '#products-section',
      actionId: 'uf-moong-1'
    },
    {
      id: 'search-dal-2',
      name: 'Desi Chana Dal (1Kg)',
      category: 'Pulses & Dal',
      type: 'product',
      price: 115,
      priceDisplay: '₹115',
      image: 'assets/images/chana-dal.svg',
      description: 'Golden, nutritious bengal gram split lentils carefully sorted and packed. Rich in dietary fiber, low glycemic index, and zinc.',
      keywords: ['dal', 'chana dal', 'pulses', 'bengal gram', 'tadka', 'fiber', 'desi'],
      url: '#products-section',
      actionId: 'uf-chana-1'
    },
    {
      id: 'search-dal-3',
      name: 'Premium Toor Dal (1Kg)',
      category: 'Pulses & Dal',
      type: 'product',
      price: 165,
      priceDisplay: '₹165',
      image: 'assets/images/toor-dal.svg',
      description: 'High-protein unpolished pigeon pea lentils for daily wholesome dal tadka, sambar, and Gujarati dal.',
      keywords: ['dal', 'toor dal', 'arhar dal', 'pulses', 'sambar', 'protein'],
      url: '#products-section',
      actionId: 'uf-toor-1'
    },

    // 4. Products - Spices
    {
      id: 'search-spice-1',
      name: 'Pure Turmeric Powder (Haldi 500g)',
      category: 'Spices',
      type: 'product',
      price: 95,
      priceDisplay: '₹95',
      image: 'assets/images/haldi-powder.svg',
      description: 'High-curcumin aromatic turmeric ground from select Kandhamal farm roots with zero added artificial colors or preservatives.',
      keywords: ['spices', 'haldi', 'turmeric', 'curcumin', 'kandhamal', 'pure masala', 'yellow'],
      url: '#products-section',
      actionId: 'uf-haldi-1'
    },

    // 5. Products - Snacks
    {
      id: 'search-snack-1',
      name: 'Traditional Odisha Mixture & Namkeen',
      category: 'Snacks',
      type: 'product',
      price: 85,
      priceDisplay: '₹85',
      image: 'assets/images/cat-snacks.jpg',
      description: 'Crunchy savory tea-time mixture fried in pure Union Foods sunflower oil with curry leaves, peanuts, and authentic spices.',
      keywords: ['snacks', 'namkeen', 'mixture', 'tea time', 'crunchy', 'munchies'],
      url: '#categories-section',
      actionId: 'cat-snacks'
    },

    // 6. Products - Beverages
    {
      id: 'search-bev-1',
      name: 'Fresh Kesar Mango Lassi & Juices',
      category: 'Beverages',
      type: 'product',
      price: 60,
      priceDisplay: '₹60',
      image: 'assets/images/food-lassi.jpg',
      description: 'Refreshing probiotic curd smoothie blended with sweet mango pulp, saffron strands, and natural cardamom.',
      keywords: ['beverages', 'lassi', 'mango', 'juice', 'kesar', 'drink', 'refreshing'],
      url: '#categories-section',
      actionId: 'cat-beverages'
    },

    // 7. Product Categories (6 Categories)
    {
      id: 'search-cat-oil',
      name: 'Cooking Oils Category',
      category: 'Categories',
      type: 'category',
      price: 0,
      priceDisplay: 'From ₹145',
      image: 'assets/images/cat-oil.jpg',
      description: 'Explore our range of heart-healthy refined sunflower oil, kachi ghani mustard oil, and cold-pressed oils.',
      keywords: ['category', 'cooking oil', 'oil', 'mustard', 'sunflower'],
      url: '#categories-section',
      actionId: 'oil'
    },
    {
      id: 'search-cat-flour',
      name: 'Flour & Grains Category',
      category: 'Categories',
      type: 'category',
      price: 0,
      priceDisplay: 'From ₹48/kg',
      image: 'assets/images/cat-flour.jpg',
      description: '100% natural Chakki fresh Sharbati whole wheat atta, multigrain atta, and nutrient-dense grain flours.',
      keywords: ['category', 'flour', 'grains', 'atta', 'wheat', 'sharbati'],
      url: '#categories-section',
      actionId: 'flour'
    },
    {
      id: 'search-cat-pulses',
      name: 'Pulses & Dal Category',
      category: 'Categories',
      type: 'category',
      price: 0,
      priceDisplay: 'From ₹115',
      image: 'assets/images/cat-pulses.jpg',
      description: 'Unpolished, naturally grown moong dal, toor dal, and desi chana dal packed with wholesome plant protein.',
      keywords: ['category', 'pulses', 'dal', 'lentils', 'moong', 'toor', 'chana'],
      url: '#categories-section',
      actionId: 'pulses'
    },
    {
      id: 'search-cat-spices',
      name: 'Pure Spices Category',
      category: 'Categories',
      type: 'category',
      price: 0,
      priceDisplay: 'From ₹45',
      image: 'assets/images/cat-spices.jpg',
      description: 'Sun-dried, high-aroma whole and powdered spices including Haldi, Dhaniya, Jeera, and Mirch.',
      keywords: ['category', 'spices', 'haldi', 'turmeric', 'chili', 'masala'],
      url: '#categories-section',
      actionId: 'spices'
    },
    {
      id: 'search-cat-snacks',
      name: 'Healthy Snacks Category',
      category: 'Categories',
      type: 'category',
      price: 0,
      priceDisplay: 'From ₹40',
      image: 'assets/images/cat-snacks.jpg',
      description: 'Crispy namkeens, roasted nuts, and wholesome tea-time snacks prepared hygienically in pure vegetable oil.',
      keywords: ['category', 'snacks', 'namkeen', 'healthy snacks'],
      url: '#categories-section',
      actionId: 'snacks'
    },
    {
      id: 'search-cat-beverages',
      name: 'Pure Beverages Category',
      category: 'Categories',
      type: 'category',
      price: 0,
      priceDisplay: 'From ₹35',
      image: 'assets/images/cat-beverages.jpg',
      description: 'Chilled natural lassi, probiotic yogurt drinks, and fresh wholesome fruit juices.',
      keywords: ['category', 'beverages', 'drinks', 'lassi', 'juice'],
      url: '#categories-section',
      actionId: 'beverages'
    },

    // 8. Special Food Offers & Discounts
    {
      id: 'search-offer-1',
      name: 'Buy 1 Get 1 Free: Premium Moong Dal',
      category: 'Offers & Deals',
      type: 'offer',
      price: 135,
      priceDisplay: 'BOGO FREE',
      image: 'assets/images/moong-dal.svg',
      description: 'Special limited time deal: Buy one unpolished yellow moong dal pack and get another pack free! Coupon: BOGO-MOONG',
      keywords: ['offer', 'discount', 'bogo', 'buy 1 get 1', 'free', 'deals', 'special offers', 'coupon'],
      url: '#offers-slider-section',
      actionId: 'uf-moong-1'
    },
    {
      id: 'search-offer-2',
      name: 'Flat 20% OFF: Refined Sunflower Oil 5L',
      category: 'Offers & Deals',
      type: 'offer',
      price: 680,
      priceDisplay: '20% OFF',
      image: 'assets/images/sunflower-oil.svg',
      description: 'Save 20% on our family economy sunflower oil 5L jar. Use coupon code SUN20 during checkout.',
      keywords: ['offer', 'discount', '20% off', 'deals', 'sunflower oil', 'coupon', 'savings'],
      url: '#offers-slider-section',
      actionId: 'uf-oil-1'
    },
    {
      id: 'search-offer-3',
      name: 'Family Essentials Combo: Flat 30% OFF',
      category: 'Offers & Deals',
      type: 'offer',
      price: 499,
      priceDisplay: '30% OFF',
      image: 'assets/images/banner-4-pantry.jpg',
      description: 'Sharbati Atta 5kg + Sunflower Oil 1L + Moong Dal 1kg at an unbeatable combo bundle price. Code: UNION30',
      keywords: ['offer', 'discount', 'combo', 'bundle', '30% off', 'family pack', 'deals'],
      url: '#offers-slider-section',
      actionId: 'uf-atta-1'
    },
    {
      id: 'search-offer-4',
      name: 'Free Express Delivery Across Odisha',
      category: 'Offers & Deals',
      type: 'offer',
      price: 0,
      priceDisplay: 'FREE SHIP',
      image: 'assets/images/cert-fssai.svg',
      description: 'Zero delivery fee on all groceries and pantry orders above ₹499 in Bhubaneswar, Cuttack, and Odisha.',
      keywords: ['free delivery', 'free shipping', 'zero delivery fee', 'express delivery', 'deals'],
      url: '#cart-drawer',
      actionId: 'cart'
    },

    // 9. Recipes
    {
      id: 'search-recipe-paneer',
      name: 'Shahi Paneer Masala Recipe',
      category: 'Recipes',
      type: 'recipe',
      price: 0,
      priceDisplay: 'Recipe Card',
      image: 'assets/images/food-paneer.jpg',
      description: 'Rich, royal cottage cheese curry simmered in a velvety gravy of cashews, tomatoes, and pure Union Foods spices.',
      keywords: ['recipe', 'paneer', 'shahi paneer', 'cooking', 'curry', 'dinner', 'lunch'],
      url: '#recipes',
      actionId: 'shahi-paneer'
    },
    {
      id: 'search-recipe-biryani',
      name: 'Vegetable Dum Biryani Recipe',
      category: 'Recipes',
      type: 'recipe',
      price: 0,
      priceDisplay: 'Recipe Card',
      image: 'assets/images/food-biryani.jpg',
      description: 'Aromatic layered basmati rice with farm vegetables, saffron, and slow-cooked sealed dum perfection.',
      keywords: ['recipe', 'biryani', 'dum biryani', 'rice', 'pulao', 'cooking'],
      url: '#recipes',
      actionId: 'biryani'
    },
    {
      id: 'search-recipe-dosa',
      name: 'Crispy Masala Dosa Recipe',
      category: 'Recipes',
      type: 'recipe',
      price: 0,
      priceDisplay: 'Recipe Card',
      image: 'assets/images/food-dosa.jpg',
      description: 'Golden fermented rice-urad crepe with spiced potato filling, coconut chutney, and piping hot sambar.',
      keywords: ['recipe', 'dosa', 'masala dosa', 'south indian', 'breakfast', 'crispy'],
      url: '#recipes',
      actionId: 'dosa'
    },
    {
      id: 'search-recipe-samosa',
      name: 'Golden Desi Samosas Recipe',
      category: 'Recipes',
      type: 'recipe',
      price: 0,
      priceDisplay: 'Recipe Card',
      image: 'assets/images/food-samosa.jpg',
      description: 'Flaky pastry triangles filled with spiced cumin potatoes and green peas, deep-fried in Union Foods sunflower oil.',
      keywords: ['recipe', 'samosa', 'snacks', 'evening snack', 'fried'],
      url: '#recipes',
      actionId: 'samosa'
    },
    {
      id: 'search-recipe-puri',
      name: 'Crispy Puri & Aloo Dum Recipe',
      category: 'Recipes',
      type: 'recipe',
      price: 0,
      priceDisplay: 'Recipe Card',
      image: 'assets/images/food-puri-sabji.jpg',
      description: 'Puffy whole wheat puris made with Sharbati atta paired with spicy baby potato dum curry.',
      keywords: ['recipe', 'puri', 'aloo dum', 'breakfast favorite', 'atta'],
      url: '#recipes',
      actionId: 'puri-sabji'
    },

    // 10. Company Information & About Us
    {
      id: 'search-info-about',
      name: 'About Union Foods - Est. 1982',
      category: 'Company Info',
      type: 'info',
      price: 0,
      priceDisplay: '40+ Years',
      image: 'assets/images/union-foods-logo.png',
      description: 'Founded in 1982, Union Foods has grown into Odisha’s premier food brand delivering pure, wholesome staples to over 500,000 households.',
      keywords: ['about', 'about us', 'company', 'union foods', 'history', 'founder', 'heritage', 'est 1982', 'odisha'],
      url: '#about',
      actionId: 'about'
    },
    {
      id: 'search-info-mission',
      name: 'Our Farm-to-Table Quality Promise',
      category: 'Company Info',
      type: 'info',
      price: 0,
      priceDisplay: 'Our Values',
      image: 'assets/images/banner-2-farmer.jpg',
      description: 'Direct procurement from trusted Indian farmers with zero middlemen, fair prices, and rigorous 7-stage quality inspection.',
      keywords: ['mission', 'values', 'quality', 'farmer', 'sustainability', 'purity'],
      url: '#why-choose',
      actionId: 'why-choose'
    },
    {
      id: 'search-info-contact',
      name: 'Contact & Customer Support',
      category: 'Company Info',
      type: 'info',
      price: 0,
      priceDisplay: '+91 98765 43210',
      image: 'assets/images/union-foods-logo.png',
      description: 'Phone: +91 98765 43210 | Email: info@unionfoods.in | Corporate HQ: Plot 42, Infocity Road, Patia, Bhubaneswar, Odisha.',
      keywords: ['contact', 'phone', 'email', 'support', 'help', 'address', 'office', 'headquarters', 'bhubaneswar'],
      url: '#contact',
      actionId: 'contact'
    },

    // 11. Certifications
    {
      id: 'search-cert-fssai',
      name: 'FSSAI License No: 10019031003214',
      category: 'Certifications',
      type: 'certification',
      price: 0,
      priceDisplay: 'Government Certified',
      image: 'assets/images/cert-fssai.svg',
      description: 'Official Food Safety and Standards Authority of India (FSSAI) license guaranteeing statutory compliance, unadulterated purity, and safety.',
      keywords: ['certification', 'fssai', 'license', 'quality', 'safety', 'government', 'standards'],
      url: '#certifications-section',
      actionId: 'fssai'
    },
    {
      id: 'search-cert-iso',
      name: 'ISO 22000 Food Safety Management',
      category: 'Certifications',
      type: 'certification',
      price: 0,
      priceDisplay: 'Global Standard',
      image: 'assets/images/cert-iso.svg',
      description: 'Internationally recognized certification for comprehensive food hygiene, traceability, and hazard management across the supply chain.',
      keywords: ['certification', 'iso', 'iso 22000', 'global', 'hygiene'],
      url: '#certifications-section',
      actionId: 'iso'
    },
    {
      id: 'search-cert-haccp',
      name: 'HACCP Hazard Control Certified',
      category: 'Certifications',
      type: 'certification',
      price: 0,
      priceDisplay: 'Zero Defect',
      image: 'assets/images/cert-haccp.svg',
      description: 'Rigorous Hazard Analysis Critical Control Point system applied across all automated milling, extraction, and sealing lines.',
      keywords: ['certification', 'haccp', 'hazard', 'safety', 'clean'],
      url: '#certifications-section',
      actionId: 'haccp'
    },

    // 12. Locations & Hubs
    {
      id: 'search-loc-bhubaneswar',
      name: 'Bhubaneswar Central Processing & Express Hub',
      category: 'Company Info',
      type: 'info',
      price: 0,
      priceDisplay: 'Hub 1',
      image: 'assets/images/facility.svg',
      description: 'Plot 42, Infocity Road, Patia, Bhubaneswar. 45,000 sq.ft state-of-the-art automated flour mill and oil packaging unit with live preview.',
      keywords: ['locations', 'bhubaneswar', 'patia', 'hub', 'processing plant', 'facility', 'map'],
      url: '#locations',
      actionId: 'bhubaneswar'
    },
    {
      id: 'search-loc-cuttack',
      name: 'Cuttack Metro Distribution Depot',
      category: 'Company Info',
      type: 'info',
      price: 0,
      priceDisplay: 'Hub 2',
      image: 'assets/images/facility.svg',
      description: 'Malgodown Commercial Zone, Cuttack. High-volume transit center catering to twin city wholesale networks and fast home delivery.',
      keywords: ['locations', 'cuttack', 'malgodown', 'depot', 'distribution'],
      url: '#locations',
      actionId: 'cuttack'
    }
  ];

  window.searchData = SEARCH_DATABASE;

  /* ==========================================================================
     SMART SEARCH LOGIC & CONTROLLER
     ========================================================================== */
  let currentSearchFilter = 'all';
  let currentSearchSort = 'relevance';
  let searchHistory = [];

  try {
    const saved = localStorage.getItem('union_search_history');
    if (saved) searchHistory = JSON.parse(saved);
  } catch (e) {
    searchHistory = ['Mustard Oil', 'Sharbati Atta', 'BOGO Offer'];
  }

  function saveSearchQuery(query) {
    if (!query || query.trim().length < 2) return;
    query = query.trim();
    searchHistory = [query, ...searchHistory.filter(q => q.toLowerCase() !== query.toLowerCase())].slice(0, 8);
    try {
      localStorage.setItem('union_search_history', JSON.stringify(searchHistory));
    } catch (e) {}
    renderSearchHistoryChips();
  }

  function clearSearchHistory() {
    searchHistory = [];
    try {
      localStorage.removeItem('union_search_history');
    } catch (e) {}
    renderSearchHistoryChips();
  }

  function removeHistoryItem(term) {
    searchHistory = searchHistory.filter(t => t.toLowerCase() !== term.toLowerCase());
    try {
      localStorage.setItem('union_search_history', JSON.stringify(searchHistory));
    } catch (e) {}
    renderSearchHistoryChips();
  }

  function renderSearchHistoryChips() {
    const block = document.getElementById('recent-searches-block');
    const container = document.getElementById('recent-chips-container');
    if (!block || !container) return;

    if (searchHistory.length === 0) {
      block.style.display = 'none';
      return;
    }

    block.style.display = 'block';
    container.innerHTML = searchHistory.map(term => `
      <span class="search-chip">
        <span onclick="window.UnionFoods.applySearchChip('${term.replace(/'/g, "\\\\'")}')">${term}</span>
        <button type="button" class="chip-remove-btn" onclick="window.UnionFoods.removeHistoryItem('${term.replace(/'/g, "\\\\'")}')" aria-label="Remove ${term}">&times;</button>
      </span>
    `).join('');
  }

  function highlightMatches(text, query) {
    if (!query || !text) return text;
    const tokens = query.toLowerCase().split(/\\s+/).filter(Boolean);
    if (!tokens.length) return text;
    const regex = new RegExp(`(${tokens.map(t => t.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')).join('|')})`, 'gi');
    return text.replace(regex, '<mark class="search-highlight">$1</mark>');
  }

  function executeSearch(query) {
    query = (query || '').trim().toLowerCase();
    const tokens = query.split(/\\s+/).filter(Boolean);

    let results = SEARCH_DATABASE.map(item => {
      let score = 0;
      if (!tokens.length) {
        // Return default recommendation score based on popularity
        score = item.type === 'product' ? 10 : (item.type === 'offer' ? 9 : 5);
        return { item, score };
      }

      const nameLower = item.name.toLowerCase();
      const catLower = item.category.toLowerCase();
      const descLower = item.description.toLowerCase();
      const kwString = (item.keywords || []).join(' ').toLowerCase();

      // Exact name match
      if (nameLower === query) score += 100;
      else if (nameLower.startsWith(query)) score += 60;
      else if (nameLower.includes(query)) score += 40;

      // Token matching
      tokens.forEach(tok => {
        if (nameLower.includes(tok)) score += 25;
        if (catLower.includes(tok)) score += 20;
        if (kwString.includes(tok)) score += 18;
        if (descLower.includes(tok)) score += 10;
      });

      return { item, score };
    });

    results = results.filter(r => r.score > 0);

    // Apply Filter
    if (currentSearchFilter !== 'all') {
      results = results.filter(r => r.item.type === currentSearchFilter);
    }

    // Apply Sorting
    if (currentSearchSort === 'price-asc') {
      results.sort((a, b) => a.item.price - b.item.price);
    } else if (currentSearchSort === 'price-desc') {
      results.sort((a, b) => b.item.price - a.item.price);
    } else if (currentSearchSort === 'name-asc') {
      results.sort((a, b) => a.item.name.localeCompare(b.item.name));
    } else {
      // Relevance
      results.sort((a, b) => b.score - a.score);
    }

    return results.map(r => r.item);
  }

  function updateFilterCounts(query) {
    const counts = { all: 0, product: 0, category: 0, offer: 0, recipe: 0, info: 0, certification: 0 };
    const q = (query || '').trim().toLowerCase();
    const tokens = q.split(/\\s+/).filter(Boolean);

    SEARCH_DATABASE.forEach(item => {
      let matches = true;
      if (tokens.length) {
        const text = (item.name + ' ' + item.category + ' ' + item.description + ' ' + (item.keywords || []).join(' ')).toLowerCase();
        matches = tokens.some(t => text.includes(t));
      }
      if (matches) {
        counts.all++;
        if (counts[item.type] !== undefined) counts[item.type]++;
      }
    });

    ['all', 'product', 'category', 'offer', 'recipe', 'info', 'certification'].forEach(t => {
      const el = document.getElementById(`count-${t}`);
      if (el) el.textContent = counts[t] || 0;
    });
  }

  function renderSearchResults(query) {
    const grid = document.getElementById('search-results-grid');
    const noResults = document.getElementById('search-no-results');
    const defaultsBox = document.getElementById('search-defaults-box');
    const statusText = document.getElementById('search-status-text');
    if (!grid) return;

    updateFilterCounts(query);
    const results = executeSearch(query);

    if (results.length === 0) {
      grid.innerHTML = '';
      if (noResults) noResults.style.display = 'block';
      if (defaultsBox) defaultsBox.style.display = 'none';
      if (statusText) statusText.textContent = `No matches found for "${query}"`;
      return;
    }

    if (noResults) noResults.style.display = 'none';
    if (defaultsBox) defaultsBox.style.display = query ? 'none' : 'block';
    if (statusText) {
      statusText.textContent = query
        ? `Found ${results.length} result${results.length === 1 ? '' : 's'} for "${query}"`
        : `Showing ${results.length} recommended items`;
    }

    grid.innerHTML = results.map(item => {
      const highlightedName = highlightMatches(item.name, query);
      const highlightedDesc = highlightMatches(item.description, query);
      const actionText = item.type === 'product' ? 'View & Buy' : (item.type === 'recipe' ? 'View Recipe' : (item.type === 'offer' ? 'Claim Deal' : 'Navigate &rarr;'));

      return `
        <div class="search-result-card" onclick="window.UnionFoods.handleResultClick('${item.id}')">
          <div class="search-card-thumb-wrap">
            <span class="search-card-badge">${item.category}</span>
            <img src="${item.image}" alt="${item.name}" class="search-card-thumb" loading="lazy">
          </div>
          <h4 class="search-card-title">${highlightedName}</h4>
          <p class="search-card-desc">${highlightedDesc}</p>
          <div class="search-card-footer">
            <span class="search-card-price">${item.priceDisplay}</span>
            <button type="button" class="search-card-action-btn">${actionText}</button>
          </div>
        </div>
      `;
    }).join('');
  }

  function handleResultClick(itemId) {
    const item = SEARCH_DATABASE.find(i => i.id === itemId);
    if (!item) return;

    closeSearchModal();

    if (item.type === 'product' && item.actionId) {
      openQuickView(item.actionId);
    } else if (item.type === 'recipe') {
      openRecipeModal(item.actionId);
    } else if (item.type === 'category') {
      filterCategory(item.actionId);
      const target = document.querySelector(item.url);
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    } else {
      const target = document.querySelector(item.url);
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    }
  }

  function openSearchModal(initialQuery = '', filter = 'all') {
    const modal = document.getElementById('search-modal');
    const input = document.getElementById('modal-search-input');
    if (!modal) return;

    currentSearchFilter = filter;
    document.querySelectorAll('.search-filter-pill').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-filter') === filter);
    });

    modal.classList.add('active');
    renderSearchHistoryChips();

    if (input) {
      input.value = initialQuery;
      const clearBtn = document.getElementById('modal-search-clear');
      if (clearBtn) clearBtn.style.display = initialQuery ? 'flex' : 'none';
      setTimeout(() => input.focus(), 150);
    }

    renderSearchResults(initialQuery);
  }

  function closeSearchModal() {
    const modal = document.getElementById('search-modal');
    if (modal) modal.classList.remove('active');
  }

  /* Live Autocomplete in Navbar */
  let activeSuggestionIndex = -1;

  function handleNavSearchInput(e) {
    const query = e.target.value.trim();
    const clearBtn = document.getElementById('nav-search-clear-btn');
    const box = document.getElementById('nav-search-suggestions');
    const list = document.getElementById('suggestions-list-box');
    if (clearBtn) clearBtn.style.display = query ? 'flex' : 'none';

    if (!query || query.length < 1) {
      if (box) box.style.display = 'none';
      return;
    }

    const matches = executeSearch(query).slice(0, 6);
    if (!matches.length) {
      if (box) box.style.display = 'none';
      return;
    }

    activeSuggestionIndex = -1;
    if (list) {
      list.innerHTML = matches.map((item, idx) => `
        <div class="suggestion-item" data-index="${idx}" onclick="window.UnionFoods.handleSuggestionClick('${item.id}')">
          <div class="suggestion-item-main">
            <img src="${item.image}" alt="${item.name}" class="suggestion-thumb">
            <div>
              <div class="suggestion-title">${highlightMatches(item.name, query)}</div>
              <small style="color: var(--text-muted); font-size: 0.75rem;">${item.category}</small>
            </div>
          </div>
          <span class="suggestion-tag">${item.priceDisplay}</span>
        </div>
      `).join('');
    }

    if (box) box.style.display = 'block';
  }

  function handleNavSearchKeydown(e) {
    const box = document.getElementById('nav-search-suggestions');
    if (!box || box.style.display === 'none') return;

    const items = box.querySelectorAll('.suggestion-item');
    if (!items.length) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      activeSuggestionIndex = (activeSuggestionIndex + 1) % items.length;
      updateActiveSuggestion(items);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      activeSuggestionIndex = (activeSuggestionIndex - 1 + items.length) % items.length;
      updateActiveSuggestion(items);
    } else if (e.key === 'Enter') {
      if (activeSuggestionIndex >= 0 && activeSuggestionIndex < items.length) {
        e.preventDefault();
        items[activeSuggestionIndex].click();
      }
    } else if (e.key === 'Escape') {
      box.style.display = 'none';
    }
  }

  function updateActiveSuggestion(items) {
    items.forEach((item, idx) => {
      item.classList.toggle('active', idx === activeSuggestionIndex);
      if (idx === activeSuggestionIndex) {
        item.scrollIntoView({ block: 'nearest' });
      }
    });
  }

  function handleHeaderSearch(e) {
    e.preventDefault();
    const input = document.getElementById('nav-search-input');
    const query = input ? input.value.trim() : '';
    const box = document.getElementById('nav-search-suggestions');
    if (box) box.style.display = 'none';

    saveSearchQuery(query);
    openSearchModal(query);
  }

  function handleSuggestionClick(itemId) {
    const box = document.getElementById('nav-search-suggestions');
    if (box) box.style.display = 'none';
    const input = document.getElementById('nav-search-input');
    if (input) saveSearchQuery(input.value);
    handleResultClick(itemId);
  }

  /* ==========================================================================
     HERO IMAGE SLIDER CONTROLLER (5/6 Auto-Scrolling Slides Below Navbar)
     ========================================================================== */
  let heroCurrentSlide = 0;
  const HERO_TOTAL_SLIDES = 6;
  let heroSlideTimer = null;

  function initHeroSlider() {
    const track = document.getElementById('hero-slider-track');
    const prevBtn = document.getElementById('hero-slider-prev');
    const nextBtn = document.getElementById('hero-slider-next');
    const dots = document.querySelectorAll('.slider-dot');
    if (!track) return;

    function goToSlide(idx) {
      heroCurrentSlide = (idx + HERO_TOTAL_SLIDES) % HERO_TOTAL_SLIDES;
      track.style.transform = `translateX(-${(heroCurrentSlide * 100) / HERO_TOTAL_SLIDES}%)`;

      document.querySelectorAll('.hero-slide').forEach((slide, i) => {
        slide.classList.toggle('active', i === heroCurrentSlide);
      });

      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === heroCurrentSlide);
      });
    }

    function startTimer() {
      stopTimer();
      heroSlideTimer = setInterval(() => {
        goToSlide(heroCurrentSlide + 1);
      }, 4500);
    }

    function stopTimer() {
      if (heroSlideTimer) clearInterval(heroSlideTimer);
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        goToSlide(heroCurrentSlide - 1);
        startTimer();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        goToSlide(heroCurrentSlide + 1);
        startTimer();
      });
    }

    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const idx = parseInt(dot.getAttribute('data-index'), 10) || 0;
        goToSlide(idx);
        startTimer();
      });
    });

    const container = document.getElementById('hero-slider');
    if (container) {
      container.addEventListener('mouseenter', stopTimer);
      container.addEventListener('mouseleave', startTimer);

      // Mobile Touch Swipe Handlers
      let startX = 0;
      let startY = 0;

      container.addEventListener('touchstart', e => {
        if (e.touches.length === 1) {
          startX = e.touches[0].clientX;
          startY = e.touches[0].clientY;
          stopTimer();
        }
      }, { passive: true });

      container.addEventListener('touchend', e => {
        if (e.changedTouches.length === 1) {
          const deltaX = e.changedTouches[0].clientX - startX;
          const deltaY = e.changedTouches[0].clientY - startY;
          if (Math.abs(deltaX) > 40 && Math.abs(deltaX) > Math.abs(deltaY)) {
            if (deltaX < 0) goToSlide(heroCurrentSlide + 1);
            else goToSlide(heroCurrentSlide - 1);
          }
          startTimer();
        }
      }, { passive: true });
    }

    goToSlide(0);
    startTimer();
  }
'''

# Find insertion point before window.UnionFoods = {
target = '  window.UnionFoods = {'
if target in js_content:
    js_content = js_content.replace(target, search_and_slider_code + '\n' + target, 1)
    print("Injected search and slider code before window.UnionFoods")
else:
    print("Warning: target not found in script.js")

# Now add exported methods into window.UnionFoods
export_target = '    openWhatsApp: () => {'
export_additions = '''    openSearchModal,
    closeSearchModal,
    applySearchChip: (query) => {
      const input = document.getElementById('modal-search-input');
      if (input) input.value = query;
      const clearBtn = document.getElementById('modal-search-clear');
      if (clearBtn) clearBtn.style.display = query ? 'flex' : 'none';
      saveSearchQuery(query);
      renderSearchResults(query);
    },
    clearSearchHistory,
    removeHistoryItem,
    handleHeaderSearch,
    handleSuggestionClick,
    handleResultClick,
    triggerSearchReSort: () => {
      const sel = document.getElementById('search-sort-select');
      if (sel) currentSearchSort = sel.value;
      const input = document.getElementById('modal-search-input');
      renderSearchResults(input ? input.value : '');
    },
'''

if export_target in js_content:
    js_content = js_content.replace(export_target, export_additions + '\n' + export_target, 1)
    print("Exported search methods to window.UnionFoods")
else:
    print("Warning: export_target not found")

# Add init listeners inside DOMContentLoaded
dom_target = '    initMap();'
dom_additions = '''    initMap();
    initHeroSlider();

    // Nav Search input listeners
    const navInput = document.getElementById('nav-search-input');
    if (navInput) {
      navInput.addEventListener('input', handleNavSearchInput);
      navInput.addEventListener('keydown', handleNavSearchKeydown);
    }
    const navClear = document.getElementById('nav-search-clear-btn');
    if (navClear) {
      navClear.addEventListener('click', () => {
        if (navInput) {
          navInput.value = '';
          navInput.focus();
        }
        navClear.style.display = 'none';
        const box = document.getElementById('nav-search-suggestions');
        if (box) box.style.display = 'none';
      });
    }

    // Modal Search input listeners
    const modalInput = document.getElementById('modal-search-input');
    const modalClear = document.getElementById('modal-search-clear');
    if (modalInput) {
      modalInput.addEventListener('input', (e) => {
        const val = e.target.value;
        if (modalClear) modalClear.style.display = val ? 'flex' : 'none';
        renderSearchResults(val);
      });
      modalInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          saveSearchQuery(modalInput.value);
        } else if (e.key === 'Escape') {
          closeSearchModal();
        }
      });
    }
    if (modalClear) {
      modalClear.addEventListener('click', () => {
        if (modalInput) {
          modalInput.value = '';
          modalInput.focus();
        }
        modalClear.style.display = 'none';
        renderSearchResults('');
      });
    }

    // Filter pills click
    document.querySelectorAll('.search-filter-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        document.querySelectorAll('.search-filter-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        currentSearchFilter = pill.getAttribute('data-filter') || 'all';
        renderSearchResults(modalInput ? modalInput.value : '');
      });
    });

    // Close suggestions on outside click
    document.addEventListener('click', (e) => {
      const wrap = document.getElementById('header-search-wrap');
      const box = document.getElementById('nav-search-suggestions');
      if (box && wrap && !wrap.contains(e.target)) {
        box.style.display = 'none';
      }
    });

    // Global Esc key closes search modal
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeSearchModal();
      }
    });
'''

if dom_target in js_content:
    js_content = js_content.replace(dom_target, dom_additions, 1)
    print("Added DOMContentLoaded event listeners for search and slider")
else:
    print("Warning: dom_target not found")

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("SUCCESS: js/script.js updated!")
