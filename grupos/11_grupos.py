import re

# + -> um ou mais
# ? -> zero ou um

texto1 = "O José Simão é muito engraçado... hehehehehehehe"

regex = re.compile(r"(he)+")

r = regex.search(texto1)

print(r.group(0))

texto2 = "http://www.site.info www.escola.ninja.br google.com.ag"

regex = re.compile(r"(http:\/\/)?(www\.)?\w+\.\w{2,}(\.\w{2})?")

r = regex.finditer(texto2)

for m in r:
    print(m.group())
