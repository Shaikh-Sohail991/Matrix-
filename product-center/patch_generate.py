import sys
import os

def djangoify_html_string():
    return """
    html = '{% load static %}\\n' + html
    html = html.replace('href="awesome.css"', 'href="{% static \\'css/awesome.css\\' %}"')
    html = html.replace('src="main.js"', 'src="{% static \\'js/product_main.js\\' %}"')
    for p in ['index', 'dc-power-supply', 'ac-power-supply', 'electronic-loads', 'lcr-meter', 'withstand-voltage-tester', 'oscilloscope', 'all-products']:
        html = html.replace(f'href="{p}.html"', f'href="{{% url \\'products:center_page\\' page_name=\\'{p}\\' %}}"')
"""

with open('generate.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Patch OUT_DIR
content = content.replace('OUT_DIR = "."', 'OUT_DIR = "../templates/product-center"')
content = content.replace('OUT_DIR = "/home/claude/product-center"', 'OUT_DIR = "../templates/product-center"')

# Patch generate_page return
if 'return html' in content and 'load static' not in content:
    patch = djangoify_html_string() + "    return html"
    content = content.replace('    return html', patch)

# Patch generate_all_products return
# It returns the f-string directly: return f"""<!DOCTYPE html>..."""
# Let's change it to:
# html = f"""<!DOCTYPE html>..."""
# then apply patch and return html
if 'return f"""<!DOCTYPE html>' in content:
    content = content.replace('    return f"""<!DOCTYPE html>', '    html = f"""<!DOCTYPE html>')
    
# Now find where generate_all_products function ends. The string ends at `</html>\n"""`
if '</html>\n"""\n' in content:
    content = content.replace('</html>\n"""\n', '</html>\n"""\n' + djangoify_html_string() + '    return html\n')

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('generate.py patched successfully.')
