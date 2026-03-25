import urllib.request
urls = [
    "https://www.szmatrix.com/wp-content/uploads/2023/04/MPS-1000-Front-1024x680.jpg",
    "https://www.szmatrix.com/wp-content/uploads/2023/04/APS-7000-1-1024x680.jpg",
    "https://www.szmatrix.com/wp-content/uploads/2023/04/PEL-8000-1-1024x680.jpg",
    "https://www.szmatrix.com/wp-content/uploads/2023/04/LCR-8000G-1-1024x680.jpg",
    "https://www.szmatrix.com/wp-content/uploads/2023/04/GPT-9000-1-1024x680.jpg",
    "https://www.szmatrix.com/wp-content/uploads/2023/04/MSO-2000-1-1024x680.jpg",
]
for u in urls:
    try:
        urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla'}))
        print(f"OK: {u}")
    except Exception as e:
        print(f"FAIL: {u} - {e}")
