import json

with open('urls.json', 'r') as f:
    urls = json.load(f)

with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace("def product_cards(products):", "def product_cards(cid, products):")
code = code.replace("product_cards(cat[\"products\"])", "product_cards(cat['id'], cat['products'])")
code = code.replace("product_cards(cat['products'])", "product_cards(cat['id'], cat['products'])")

img_map_code = "IMAGES_MAP = " + json.dumps(urls, indent=4) + "\\n\\n"
if "IMAGES_MAP =" not in code:
    code = code.replace("import os", "import os\\n" + img_map_code)

img_replacement = """<img src=\"{IMAGES_MAP.get(cid, '')}\" alt=\"{p['name']}\" style=\"width:100%; height:100%; object-fit:cover;\">"""
code = code.replace("<span class=\"img-placeholder\">{p['model'][0]}</span>", img_replacement)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate.py successfully patched to use real images.")
