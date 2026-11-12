# Union Foods - Fully Responsive & Dynamic Website

> **Reference Design:** `ProvidedUnionFoodsWebsiteDesignTemplate`  
> **Technology Stack:** Pure HTML5, CSS3, Vanilla JavaScript (ES6+)  
> **Frameworks:** Zero external libraries/frameworks (No Bootstrap, Tailwind, or React)  
> **Responsiveness:** Fully mobile-first, verified across 320px to 1920px+ viewports  

---

## 🌾 Project Overview

This repository contains the complete, production-ready website developed for **Union Foods Private Limited** (Bhubaneswar, Odisha). The project strictly reproduces the layout, color palette, typography, visual hierarchy, and component structure from the provided reference design while incorporating 45+ interactive features, smooth micro-interactions, and comprehensive mobile-first responsiveness.

---

## 🎨 Visual Identity & Reference Design Fidelity

Every section from the reference design template has been faithfully implemented:

1. **Top Utility Bar**: Direct contact hotline (`+91 98765 43210`), support email (`info@unionfoods.in`), corporate location (`Bhubaneswar, Odisha, India`), official social media links, plus live Theme and Language toggles.
2. **Main Navigation**: High-resolution vector logo with organic leaf emblem, clean navigation menu with category dropdowns, live instant search trigger, animated shopping cart badge (`0`), and orange pill CTA button (`Order Now`).
3. **Section 16 - Continuous Food Marquee**: Smooth infinite scrolling image gallery directly below the navigation bar featuring culinary highlights (Puri Sabji, Shahi Paneer, Biryani, Masala Dosa, Samosas, Lassi, Salad, Gulab Jamun) with hover zoom and pause-on-hover.
4. **Hero Banner**: *"Pure Food for a Healthier Life"*, warm wheat field sunlit atmosphere, floating product showcase (*Refined Sunflower Oil*, *Premium Atta*, *Moong Dal*, *Chana Dal*), and dual call-to-action buttons.
5. **Value Proposition Strip**: 6 trust pillars (*100% Hygienic & Safe*, *Premium Quality*, *Wide Range of Products*, *Reliable Delivery*, *Customer Support*, *Sustainable & Eco-Friendly*).
6. **Section 17 - Promotional Offers Marquee**: Scrolling promotional cards (*Buy 1 Get 1 Free*, *20% Off 5L Jar*, *Flat 30% Off Family Combo*, *Free Delivery*), real-time ticking countdown timer, and claim code engine.
7. **Our Product Categories**: 7 custom-illustrated category cards (*Cooking Oil*, *Flour & Grains*, *Pulses & Dal*, *Spices*, *Snacks*, *Beverages*, *Packaged Foods*) with active filtering.
8. **About Us Section**: Organic curved frame featuring the Union Foods modern processing facility and corporate headquarters in Bhubaneswar, with key highlights (*Quality Ingredients*, *Hygienic Processing*, *Trusted by Families*, *Sustainable Sourcing*).
9. **Our Featured Products**: Interactive cards with packaging size tags, price discounts, and quick-add actions.
10. **Interactive Catalog & Filter Engine**: Real-time category filtering, alphabetical and price-based sorting, and dietary preference tags.
11. **"Why Choose Union Foods?" Ribbon**: Full-width forest-green ribbon with 5 vertical dividers (*Farm to Home*, *Assured Quality*, *Modern Processing*, *No Harmful Additives*, *Trusted by Thousands*).
12. **Tasty Recipes Showcase**: Dish presentation with glowing video play button, recipe drawer, and dynamic serving size scaler.
13. **3-Column Trust & Updates Section**:
    - *Column 1*: Customer Testimonials carousel (Priya Mishra review with rating stars and controls).
    - *Column 2*: Latest News & Events with thumbnails and expansion arrows.
    - *Column 3*: Official Certifications (FSSAI license, ISO 9001:2015 / 22000 FSMS, HACCP).
14. **Batch Traceability & Odisha Pincode Checkers**: Farm-to-home batch verification scanner (`UF-2026-WHEAT`, `UF-2026-OIL`) and PIN code delivery estimator.
15. **FAQ Accordion & Statistics Counters**: Expandable questions with animated counter milestones.
16. **Newsletter Subscription Bar**: Golden harvest wheat gradient with regex validation and celebratory toast feedback.
17. **Master 5-Column Footer**: Brand biography, quick links, product catalog links, support policies, office address, and social links.

---

## ⚡ 45+ Unique Interactive Features

| Category | Features |
|---|---|
| **A. Navigation & Browsing** | 1. Sticky Navigation Bar with Elevation<br>2. Responsive Hamburger Menu<br>3. Smooth Scrolling Navigation<br>4. Active Navigation Highlighting (Scroll Spy)<br>5. Dropdown Navigation Menus<br>6. Back-to-Top Button<br>7. Scroll Progress Indicator Bar<br>8. Instant Search & Autocomplete Modal<br>9. Scroll-Triggered Reveal Animations<br>10. Breadcrumb Context Updates |
| **B. Food & Promotions** | 11. Infinite Scrolling Food Image Gallery (Below Navbar)<br>12. Image Hover Zoom & Lens Effect<br>13. Food Image Lightbox Modal<br>14. Category Filtering Engine<br>15. Automatic Promotional Offer Slider<br>16. Previous / Next Offer Controls<br>17. Live Offer Countdown Timer<br>18. Offer Detail & Coupon Popup<br>19. Featured Food Carousel<br>20. Testimonials Carousel |
| **C. Ordering & Cart** | 21. Interactive Food Menu with Custom Cards<br>22. Add-to-Cart Functionality<br>23. Shopping Cart Counter Badge with Pop Animation<br>24. Quantity Increment / Decrement (+ / -)<br>25. Remove-from-Cart with Notification<br>26. Dynamic Price Calculation (Subtotal, Tax, Shipping, Total)<br>27. Slide-over Cart Drawer<br>28. Wishlist Heart Toggle & Persistence<br>29. Food Customization (Packaging size selectors)<br>30. Coupon Code Engine (`UNION10`, `FREESHIP`, `FESTIVE20`)<br>31. Multi-parameter Sorting (Price, Rating, Name)<br>32. Friendly Empty Cart State with CTA |
| **D. User Engagement** | 33. Newsletter Validation & Subscription Confetti<br>34. Contact Form Validation with Instant Feedback<br>35. FAQ Accordion with ARIA Attributes<br>36. Interactive Customer Star Rating Widget<br>37. Floating WhatsApp Support Widget<br>38. Dark / Light Mode Theme Toggle<br>39. Custom Toast Notification System<br>40. Smooth Page Loading Transition<br>41. Animated Statistics Counters<br>42. Trilingual Language Switcher (EN / HI / OD)<br>43. Social Media Tooltips & Links<br>44. Odisha Pincode Delivery Estimator<br>45. Complete Simulated Order Confirmation Workflow |

---

## 📱 Responsive Verification Benchmarks

The website uses flexible Flexbox, CSS Grid, and fluid typography (`clamp()`) to adapt automatically to every screen size:

- **Large Desktop (1920px & 1440px):** Full multi-column grid, high-definition vector typography, and max-width container constraints.
- **Laptops (1366px & 1280px):** Balanced proportions, optimized hero graphic scaling.
- **Tablets (1024px & 768px):** 2-to-3 column grids, touch-friendly carousel drag, smooth off-canvas navigation.
- **Smartphones (430px, 390px, 375px, 360px, 320px):** Single-column layout, touch-optimized button hit targets (min 44px), zero horizontal overflow, stacked checkout drawers.

---

## 🚀 How to Run Locally

1. Clone or extract the project directory.
2. Open `index.html` directly in any modern web browser (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari).
3. No local build step, Node.js runtime, or server required!

---

## 🌐 Deployment Instructions

### Option 1: GitHub Pages
1. Push this folder to a GitHub repository.
2. Go to **Settings > Pages**.
3. Under **Branch**, select `main` and `/ (root)`, then click **Save**.
4. Your website will be live at `https://<username>.github.io/<repo-name>/`.

### Option 2: Netlify
1. Log in to [Netlify](https://www.netlify.com).
2. Drag and drop the `Union-Foods-Website` folder into the Netlify dashboard.
3. Your website deploys instantly with a free SSL certificate.

### Option 3: Vercel
1. Install Vercel CLI (`npm i -g vercel`) or import the Git repository.
2. Run `vercel` in the project root directory.
3. Deploy with zero configuration.

---

## 📄 License & Attribution
&copy; 2026 Union Foods Private Limited. All Rights Reserved.  
Crafted with pure HTML5, CSS3, and JavaScript.
