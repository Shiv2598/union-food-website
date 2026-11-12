from PIL import Image
import os

dest_dir = r'C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\images'
upload_dir = r'C:\Users\ASUS\.gemini\antigravity\brain\04dc5cee-e6bc-4573-8108-f3885bdb5342\.user_uploaded'

# 1. Load Podium
podium = Image.open(os.path.join(upload_dir, 'media_1794484350417.png')).convert('RGBA')

# 2. Load Products Image (644 x 327)
prod_img = Image.open(os.path.join(upload_dir, 'media_1794481049621.jpg')).convert('RGBA')
W, H = prod_img.size

# Clean crop of the products on table
cluster = prod_img.crop((35, 10, W - 10, H - 25))
# Target width ~560 on the 969-wide podium
target_w = 560
target_h = int(cluster.height * (target_w / cluster.width))
cluster_resized = cluster.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Paste on podium pedestal
paste_x = (podium.width - target_w) // 2
paste_y = 440 - target_h

showcase = podium.copy()
showcase.paste(cluster_resized, (paste_x, paste_y), cluster_resized)
showcase.save(os.path.join(dest_dir, 'podium-products-showcase.png'), 'PNG')
print('Saved podium-products-showcase.png:', showcase.size)

# 3. Extract individual product pack images
prod1_oil = prod_img.crop((30, 10, 160, H - 35))
prod2_atta = prod_img.crop((145, 15, 330, H - 35))
prod3_dal = prod_img.crop((315, 60, 450, H - 35))
prod4_spices = prod_img.crop((435, 70, 545, H - 35))
prod5_snacks = prod_img.crop((525, 110, 638, H - 35))

prod1_oil.convert('RGB').save(os.path.join(dest_dir, 'prod-oil.jpg'), 'JPEG', quality=95)
prod2_atta.convert('RGB').save(os.path.join(dest_dir, 'prod-atta.jpg'), 'JPEG', quality=95)
prod3_dal.convert('RGB').save(os.path.join(dest_dir, 'prod-dal.jpg'), 'JPEG', quality=95)
prod4_spices.convert('RGB').save(os.path.join(dest_dir, 'prod-spices.jpg'), 'JPEG', quality=95)
prod5_snacks.convert('RGB').save(os.path.join(dest_dir, 'prod-snacks.jpg'), 'JPEG', quality=95)

print('Successfully extracted and saved all 5 product pack images!')
