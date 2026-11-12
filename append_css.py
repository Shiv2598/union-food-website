with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

new_styles = '''
/* ==========================================================================
   ENHANCED STYLES: SMART SEARCH, HERO SLIDER, LOGO & RESPONSIVE POLISH
   ========================================================================== */

/* Brand Logo Sizing & Footer Adaptation */
.brand-logo-img {
  height: 52px;
  max-height: 58px;
  width: auto;
  object-fit: contain;
  transition: transform var(--transition-base);
}

.footer-logo-img {
  height: 54px;
  max-height: 60px;
  width: auto;
  object-fit: contain;
  transition: transform var(--transition-base);
  filter: drop-shadow(0 2px 6px rgba(0, 0, 0, 0.4));
}

/* --------------------------------------------------------------------------
   5. BELOW-NAVBAR HERO IMAGE SLIDER (5/6 Auto-Scrolling Images)
   -------------------------------------------------------------------------- */
.hero-slider-section {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: #0f172a;
}

.hero-slider-container {
  position: relative;
  width: 100%;
  height: clamp(340px, 48vw, 620px);
  min-height: 320px;
  overflow: hidden;
}

.hero-slider-track {
  display: flex;
  width: 600%;
  height: 100%;
  transition: transform 0.65s cubic-bezier(0.25, 1, 0.5, 1);
  will-change: transform;
}

.hero-slide {
  position: relative;
  width: 16.666667%;
  height: 100%;
  overflow: hidden;
}

.hero-slide-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transform: scale(1.02);
  transition: transform 6s ease;
}

.hero-slide.active .hero-slide-img {
  transform: scale(1.08);
}

.hero-slide-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    rgba(14, 23, 42, 0.88) 0%,
    rgba(14, 23, 42, 0.65) 45%,
    rgba(14, 23, 42, 0.2) 100%
  );
  display: flex;
  align-items: center;
}

.slide-content-box {
  max-width: 680px;
  color: #ffffff;
  padding: 1.5rem 0;
  animation: slideFadeIn 0.7s ease;
}

@keyframes slideFadeIn {
  from { opacity: 0; transform: translateY(18px); }
  to { opacity: 1; transform: translateY(0); }
}

.slide-tag {
  display: inline-block;
  background: rgba(240, 90, 34, 0.92);
  color: #ffffff;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-pill);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 0.85rem;
  box-shadow: 0 4px 12px rgba(240, 90, 34, 0.35);
}

.slide-heading {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.75rem, 3.8vw, 3.2rem);
  font-weight: 800;
  line-height: 1.15;
  color: #ffffff;
  margin-bottom: 0.85rem;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
}

.slide-desc {
  font-size: clamp(0.92rem, 1.3vw, 1.12rem);
  color: #e2e8f0;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  max-width: 580px;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.4);
}

.slide-cta-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

/* Slider Controls */
.slider-arrow-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.88);
  color: #1e293b;
  border: 1px solid rgba(255, 255, 255, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: all var(--transition-base);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

.slider-arrow-btn:hover {
  background: var(--primary-orange);
  color: #ffffff;
  transform: translateY(-50%) scale(1.08);
}

.slider-arrow-btn svg {
  width: 22px;
  height: 22px;
  fill: currentColor;
}

.slider-arrow-btn.prev {
  left: 1.25rem;
}

.slider-arrow-btn.next {
  right: 1.25rem;
}

.slider-dots {
  position: absolute;
  bottom: 1.25rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 0.6rem;
  z-index: 10;
  background: rgba(0, 0, 0, 0.35);
  padding: 0.4rem 0.8rem;
  border-radius: var(--radius-pill);
  backdrop-filter: blur(6px);
}

.slider-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.45);
  border: none;
  cursor: pointer;
  transition: all var(--transition-base);
}

.slider-dot.active {
  width: 28px;
  border-radius: var(--radius-pill);
  background: var(--primary-orange);
}

/* --------------------------------------------------------------------------
   SMART SEARCH BAR IN NAVBAR (Desktop / Tablet)
   -------------------------------------------------------------------------- */
.header-search-wrap {
  position: relative;
  flex: 0 1 320px;
  margin: 0 1rem;
}

.header-search-form {
  width: 100%;
}

.search-input-shell {
  display: flex;
  align-items: center;
  background: var(--bg-warm);
  border: 1.5px solid var(--border-light);
  border-radius: var(--radius-pill);
  padding: 0.3rem 0.75rem 0.3rem 0.85rem;
  transition: all var(--transition-base);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.04);
}

.search-input-shell:focus-within {
  border-color: var(--primary-orange);
  background: #ffffff;
  box-shadow: 0 0 0 3px rgba(240, 90, 34, 0.15);
}

.search-prefix-icon {
  display: flex;
  align-items: center;
  color: var(--text-muted);
  margin-right: 0.5rem;
}

.search-prefix-icon svg {
  width: 18px;
  height: 18px;
  fill: currentColor;
}

.nav-search-input {
  flex: 1;
  border: none;
  background: transparent;
  font-family: inherit;
  font-size: 0.86rem;
  color: var(--text-heading);
  outline: none;
  width: 100%;
}

.nav-search-input::placeholder {
  color: var(--text-light);
}

.nav-search-clear-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  padding: 0.2rem;
  border-radius: 50%;
  transition: color var(--transition-fast);
}

.nav-search-clear-btn:hover {
  color: #dc2626;
}

.nav-search-clear-btn svg {
  width: 14px;
  height: 14px;
  fill: currentColor;
}

.nav-search-submit-btn {
  background: var(--primary-orange);
  border: none;
  border-radius: 50%;
  width: 26px;
  height: 26px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  cursor: pointer;
  margin-left: 0.35rem;
  transition: background var(--transition-fast);
}

.nav-search-submit-btn:hover {
  background: var(--primary-orange-hover);
}

.nav-search-submit-btn svg {
  width: 13px;
  height: 13px;
  fill: currentColor;
}

/* Autocomplete Suggestions Popup */
.nav-search-suggestions {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  right: 0;
  background: var(--bg-card);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--border-light);
  z-index: 1200;
  max-height: 380px;
  overflow-y: auto;
  animation: fadeInDown 0.2s ease;
}

@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-6px); }
  to { opacity: 1; transform: translateY(0); }
}

.suggestions-header {
  padding: 0.55rem 0.85rem;
  font-size: 0.74rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  border-bottom: 1px solid var(--border-subtle);
  background: var(--bg-warm);
}

.suggestions-list-box {
  display: flex;
  flex-direction: column;
}

.suggestion-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.6rem 0.85rem;
  border-bottom: 1px solid var(--border-subtle);
  cursor: pointer;
  transition: background var(--transition-fast);
}

.suggestion-item:hover,
.suggestion-item.active {
  background: var(--primary-orange-light);
}

.suggestion-item-main {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}

.suggestion-thumb {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  object-fit: contain;
  background: #ffffff;
  padding: 2px;
  border: 1px solid var(--border-subtle);
}

.suggestion-title {
  font-size: 0.86rem;
  font-weight: 600;
  color: var(--text-heading);
}

.suggestion-tag {
  font-size: 0.72rem;
  color: var(--primary-orange);
  background: rgba(240, 90, 34, 0.1);
  padding: 0.15rem 0.5rem;
  border-radius: var(--radius-pill);
  font-weight: 600;
}

.suggestions-footer {
  padding: 0.45rem 0.85rem;
  font-size: 0.72rem;
  color: var(--text-light);
  background: var(--bg-warm);
  border-top: 1px solid var(--border-subtle);
  text-align: right;
}

.suggestions-footer kbd {
  background: rgba(0, 0, 0, 0.08);
  padding: 1px 4px;
  border-radius: 3px;
  font-family: inherit;
  font-size: 0.7rem;
}

/* --------------------------------------------------------------------------
   SMART SEARCH MODAL & FULL-SITE DASHBOARD
   -------------------------------------------------------------------------- */
.search-modal-box {
  max-width: 980px !important;
  width: 95% !important;
  max-height: 90vh !important;
  padding: 2rem !important;
  display: flex;
  flex-direction: column;
}

.search-modal-header {
  margin-bottom: 1.25rem;
}

.search-title-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.25rem;
}

.search-brand-mark {
  height: 38px;
  width: auto;
  object-fit: contain;
}

.search-modal-heading {
  font-size: clamp(1.3rem, 2.2vw, 1.8rem);
  font-weight: 800;
  color: var(--text-heading);
}

.search-modal-sub {
  font-size: 0.88rem;
  color: var(--text-muted);
  margin-bottom: 1.25rem;
}

.search-bar-composite {
  display: flex;
  align-items: center;
  background: var(--bg-warm);
  border: 2px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 0.5rem 1rem;
  margin-bottom: 1rem;
  transition: all var(--transition-base);
}

.search-bar-composite:focus-within {
  border-color: var(--primary-orange);
  background: #ffffff;
  box-shadow: 0 0 0 4px rgba(240, 90, 34, 0.15);
}

.search-composite-icon {
  display: flex;
  align-items: center;
  color: var(--primary-orange);
  margin-right: 0.75rem;
}

.search-composite-icon svg {
  width: 22px;
  height: 22px;
  fill: currentColor;
}

.modal-search-input {
  flex: 1;
  border: none;
  background: transparent;
  font-size: 1.05rem;
  font-family: inherit;
  color: var(--text-heading);
  outline: none;
}

.search-clear-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 0.35rem;
  display: flex;
  align-items: center;
  border-radius: 50%;
  transition: color var(--transition-fast);
}

.search-clear-btn:hover {
  color: #dc2626;
}

.search-clear-btn svg {
  width: 18px;
  height: 18px;
  fill: currentColor;
}

/* Filter Pills */
.search-filter-pills {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
  margin-bottom: 0.85rem;
  scrollbar-width: thin;
}

.search-filter-pill {
  white-space: nowrap;
  background: var(--bg-warm);
  border: 1px solid var(--border-light);
  color: var(--text-heading);
  font-size: 0.82rem;
  font-weight: 600;
  padding: 0.4rem 0.9rem;
  border-radius: var(--radius-pill);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.search-filter-pill:hover {
  border-color: var(--primary-orange);
  color: var(--primary-orange);
}

.search-filter-pill.active {
  background: var(--primary-orange);
  border-color: var(--primary-orange);
  color: #ffffff;
  box-shadow: 0 2px 8px rgba(240, 90, 34, 0.3);
}

/* Toolbar */
.search-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.82rem;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 0.65rem;
}

.search-sort-wrap {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.search-sort-select {
  border: 1px solid var(--border-light);
  border-radius: var(--radius-sm);
  padding: 0.25rem 0.5rem;
  font-family: inherit;
  font-size: 0.82rem;
  background: var(--bg-card);
  color: var(--text-heading);
  cursor: pointer;
}

/* Search Modal Body */
.search-modal-body {
  flex: 1;
  overflow-y: auto;
  padding-top: 1rem;
}

/* Chips Blocks */
.search-chips-block {
  margin-bottom: 1.25rem;
}

.search-chips-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-heading);
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.clear-history-btn {
  background: transparent;
  border: none;
  color: #dc2626;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  text-decoration: underline;
}

.search-chips-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.search-chip {
  background: var(--bg-warm);
  border: 1px solid var(--border-light);
  color: var(--text-heading);
  font-size: 0.82rem;
  font-weight: 500;
  padding: 0.35rem 0.8rem;
  border-radius: var(--radius-pill);
  cursor: pointer;
  transition: all var(--transition-fast);
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.search-chip:hover {
  background: var(--primary-orange-light);
  border-color: var(--primary-orange);
  color: var(--primary-orange);
}

.chip-remove-btn {
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 0.9rem;
  line-height: 1;
}

.chip-remove-btn:hover {
  color: #dc2626;
}

/* Search Results Grid (Responsive 4-col desktop, 2-3 col tablet, 1-2 col mobile) */
.search-results-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.1rem;
}

@media (max-width: 1024px) {
  .search-results-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .search-results-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 0.85rem;
  }
}

@media (max-width: 480px) {
  .search-results-grid {
    grid-template-columns: 1fr;
  }
}

/* Result Card */
.search-result-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 1rem;
  display: flex;
  flex-direction: column;
  transition: all var(--transition-base);
  box-shadow: var(--shadow-sm);
  position: relative;
}

.search-result-card:hover {
  transform: translateY(-4px);
  border-color: var(--primary-orange);
  box-shadow: var(--shadow-md);
}

.search-card-thumb-wrap {
  width: 100%;
  height: 120px;
  background: var(--bg-warm);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.75rem;
  overflow: hidden;
  position: relative;
}

.search-card-thumb {
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
  transition: transform var(--transition-base);
}

.search-result-card:hover .search-card-thumb {
  transform: scale(1.06);
}

.search-card-badge {
  position: absolute;
  top: 8px;
  left: 8px;
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.95);
  padding: 0.15rem 0.5rem;
  border-radius: var(--radius-pill);
  color: var(--primary-orange);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}

.search-card-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--text-heading);
  margin-bottom: 0.35rem;
  line-height: 1.3;
}

.search-card-desc {
  font-size: 0.78rem;
  color: var(--text-muted);
  line-height: 1.45;
  margin-bottom: 0.75rem;
  flex: 1;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.search-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border-subtle);
  padding-top: 0.65rem;
  margin-top: auto;
}

.search-card-price {
  font-size: 0.98rem;
  font-weight: 800;
  color: var(--primary-orange);
}

.search-card-action-btn {
  background: var(--primary-orange-light);
  color: var(--primary-orange);
  border: 1px solid var(--primary-orange);
  border-radius: var(--radius-sm);
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.3rem 0.65rem;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.search-card-action-btn:hover {
  background: var(--primary-orange);
  color: #ffffff;
}

/* Keyword Highlighting */
mark.search-highlight {
  background: #fef08a;
  color: #854d0e;
  padding: 0 2px;
  border-radius: 2px;
  font-weight: 700;
}

/* No Results Box */
.search-no-results {
  text-align: center;
  padding: 3rem 1.5rem;
}

.no-results-icon {
  margin-bottom: 1rem;
}

.search-no-results h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--text-heading);
  margin-bottom: 0.5rem;
}

.search-no-results p {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 1.25rem;
}

.no-results-quick-links {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.btn-sm-tag {
  background: var(--bg-warm);
  border: 1px solid var(--border-light);
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-pill);
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  color: var(--text-heading);
  transition: all var(--transition-fast);
}

.btn-sm-tag:hover {
  background: var(--primary-orange);
  color: #ffffff;
  border-color: var(--primary-orange);
}

/* Responsive search triggers */
.mobile-search-btn {
  display: none;
}

@media (max-width: 900px) {
  .header-search-wrap {
    display: none;
  }
  .mobile-search-btn {
    display: inline-flex;
  }
}
'''

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(new_styles)

print('Appended new styles to css/style.css successfully!')
