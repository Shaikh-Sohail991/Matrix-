import urllib.request
import re
import json

urls = {
    "dc-power-supply": "https://www.szmatrix.com/product-category/dc-power-supply/",
    "ac-power-supply": "https://www.szmatrix.com/product-category/ac-power-source/",
    "electronic-loads": "https://www.szmatrix.com/product-category/electronic-load/",
    "lcr-meter": "https://www.szmatrix.com/product-category/lcr-meter/",
    "withstand-voltage-tester": "https://www.szmatrix.com/product-category/withstand-voltage-tester/",
    "oscilloscope": "https://www.szmatrix.com/product-category/oscilloscope/"
}

images = {}

for cat, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+wp-content/uploads/[^"\']+(?:png|jpg|jpeg|webp))["\']', html)
        if imgs:
            valid_imgs = [i for i in imgs if 'logo' not in i.lower() and 'icon' not in i.lower()]
            product_imgs = [i for i in valid_imgs if re.search(r'\d+x\d+', i)]
            if product_imgs:
                images[cat] = product_imgs[0]
            elif valid_imgs:
                images[cat] = valid_imgs[0]
            else:
                images[cat] = imgs[0]
        else:
            images[cat] = None
    except Exception as e:
        images[cat] = "ERROR: " + str(e)

print(json.dumps(images, indent=2))
