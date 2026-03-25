import re

def fix(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the dynamic aria-current matching logic which causes lines to exceed wrap length
    content = re.sub(r'{%\s*if request\.resolver_match\.url_name\s*==[^%]+%}\s*aria-current="page"\s*{%\s*endif\s*%}', '', content, flags=re.DOTALL)
    
    # 2. Fix split Django tags: find any {% ... %} tag and replace newlines inside it with space
    def fix_tag(match):
        return match.group(0).replace('\n', ' ').replace('\r', ' ')
        
    content = re.sub(r'{%[^%]+%}', fix_tag, content)

    # 3. For index.html: ensure the feature description tags are on their own lines
    content = content.replace('{{ feat.title }}{% if feat.description %} - {{', '{{ feat.title }}\n{% if feat.description %} - {{')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix('c:/Users/MD SOHAIL/Downloads/matrix (1)/matrix/templates/base.html')
fix('c:/Users/MD SOHAIL/Downloads/matrix (1)/matrix/templates/index.html')
print("Templates fixed!")
