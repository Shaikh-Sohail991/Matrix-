import urllib.parse

with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the previous <img src="{IMAGES_MAP.get(cat['id'], '')}" ...
# with a dynamic placehold.co URL
# We need to find the <img tag in product_cards and replace it.
# To make it safe, we'll use string replacement.

old_img_tag = """<img src="{IMAGES_MAP.get(cat['id'], '')}" alt="{p['name']}" style="width:100%; height:100%; object-fit:cover;">"""
new_img_tag = """<img src="https://placehold.co/600x400/112040/00C2FF.png?text={p['model']}" alt="{p['name']}" style="width:100%; height:100%; object-fit:cover; opacity: 0.8;">"""

if old_img_tag in code:
    code = code.replace(old_img_tag, new_img_tag)
else:
    # try the cid version if it was left behind
    old_img_tag_cid = """<img src="{IMAGES_MAP.get(cid, '')}" alt="{p['name']}" style="width:100%; height:100%; object-fit:cover;">"""
    code = code.replace(old_img_tag_cid, new_img_tag)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate.py patched to use dynamic placeholders.")
