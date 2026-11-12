from PIL import Image
import numpy as np
import os

src_path = r'C:\Users\ASUS\.gemini\antigravity\brain\04dc5cee-e6bc-4573-8108-f3885bdb5342\.user_uploaded\media_1794483436345.png'
dest_dir = r'C:\Users\ASUS\.gemini\antigravity\scratch\union_foods_website\assets\images'

img = Image.open(src_path).convert('RGBA')
arr = np.array(img)

# Full banner crop
banner_crop = img.crop((20, 225, 1004, 540))
banner_crop.save(os.path.join(dest_dir, 'certifications-banner.png'), 'PNG')
print('Saved certifications-banner.png:', banner_crop.size)

# Find precise bounding boxes of the 3 seals
# Seal 1 (FSSAI): x in [25, 340]
# Seal 2 (ISO): x in [350, 675]
# Seal 3 (HACCP): x in [680, 1000]

seal1 = img.crop((25, 230, 335, 535))
seal2 = img.crop((355, 230, 665, 535))
seal3 = img.crop((690, 230, 1000, 535))

seal1.save(os.path.join(dest_dir, 'cert-fssai.png'), 'PNG')
seal2.save(os.path.join(dest_dir, 'cert-iso.png'), 'PNG')
seal3.save(os.path.join(dest_dir, 'cert-haccp.png'), 'PNG')

print('Extracted cert-fssai.png:', seal1.size)
print('Extracted cert-iso.png:', seal2.size)
print('Extracted cert-haccp.png:', seal3.size)
