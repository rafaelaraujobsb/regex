import re

texto = "supermercado superação hiperMERCADO Mercado"

# match com tudo que vem depois de super
# Positive lookbehind
regex = re.compile(r"(?<=super)[\wÀ-ú]+", re.IGNORECASE)

r = regex.findall(texto)

print(r)

# match com tudo que não tem super e tem mercado
# Negative lookbehind
regex = re.compile(r"(?<!super)mercado", re.IGNORECASE)

r = regex.findall(texto)

print(r)