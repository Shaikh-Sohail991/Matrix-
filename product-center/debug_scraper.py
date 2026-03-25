import urllib.request
import re

url = "https://www.szmatrix.com/product-category/dc-power-supply/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')

# Find all images
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
for img in imgs:
    if 'logo' not in img.lower() and 'wp-content/uploads' in img:
        print(img)
