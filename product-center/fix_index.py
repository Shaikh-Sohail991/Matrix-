import os

path = r'..\templates\product-center\index.html'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

if '{% load static %}' not in text:
    text = '{% load static %}\n' + text

text = text.replace('href="awesome.css"', 'href="{% static ' + "'css/awesome.css'" + ' %}"')
text = text.replace('src="main.js"', 'src="{% static ' + "'js/product_main.js'" + ' %}"')

pages = ['index', 'dc-power-supply', 'ac-power-supply', 'electronic-loads', 'lcr-meter', 'withstand-voltage-tester', 'oscilloscope', 'all-products']
for p in pages:
    text = text.replace('href="' + p + '.html"', 'href="{% url ' + "'products:center_page'" + ' page_name=' + "'" + p + "'" + ' %}"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("index.html patched.")
