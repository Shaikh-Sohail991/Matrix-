import urllib.request
import re
import json

urls = {
    "dc-power-supply": "https://www.szmatrix.com/product-category/dc-power-supply/",
    "ac-power-supply": "https://www.szmatrix.com/product-category/ac-power-source/",
    "electronic-loads": "https://www.szmatrix.com/product-category/electronic-load/",
    "lcr-meter": "https://www.szmatrix.com/product-category/lcr-meter/",
}

images = {}
fallback = "https://www.szmatrix.com/wp-content/uploads/2020/12/logo-2.png"

for cat, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+wp-content/uploads/[^"\']+(?:jpg|jpeg|png|webp))["\']', html)
        valid = [i for i in imgs if 'logo' not in i.lower() and 'icon' not in i.lower()]
        prod = [i for i in valid if re.search(r'\d+x\d+', i)]
        images[cat] = prod[0] if prod else valid[0] if valid else fallback
    except:
        images[cat] = fallback

images["withstand-voltage-tester"] = fallback
images["oscilloscope"] = fallback
images["all-products"] = fallback

with open('urls.json', 'w') as f:
    json.dump(images, f, indent=2)
print("Saved to urls.json")
