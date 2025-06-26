import re

def load_country_txt(ruta):
    pattern = re.compile(r'<option value="(.+?)">(.*?)</option>')
    choices = []

    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            match = pattern.search(linea)
            if match:
                value = match.group(1).strip()
                label = match.group(2).strip()
                choices.append((value, label))
    
    return choices