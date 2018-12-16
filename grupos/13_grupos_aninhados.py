import re

def view(r):
    x = list()
    for m in r:
        x.append(m.group())

    print(x)

texto = "supermercado hipermercado minimercado mercado"

regex = re.compile(r"(super|hiper|mini)?mercado")

r = regex.finditer(texto)

view(r)
