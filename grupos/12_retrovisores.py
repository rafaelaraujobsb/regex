import re

# * -> zero ou muitos
# \1 -> retrovisor, acessa o primeiro grupo
# ?: -> cria um grupo e não armazena ele
# .sub(r"\2", t) -> substitui pelo grupo 2

def view(r):
    x = list()
    for m in r:
        x.append(m.group())

    print(x)

texto1 = "<b>Destaque</b><strong>Forte</strong><div>Conteudo</div>"

regex = re.compile(r"<(\w+)>.*<\/\1>")

r = regex.finditer(texto1)

view(r)

#####

texto2 = "Lentamente é mente muito lenta."

regex = re.compile(r"(lenta)(mente).*\2.*\1\.", re.IGNORECASE)

r = regex.finditer(texto2)

view(r)

#####

regex = re.compile(r"(?:lenta)(mente).*\1", re.IGNORECASE)

r = regex.finditer(texto2)

view(r)

####

regex = re.compile(r"(lenta)(mente)?", re.IGNORECASE)

r = regex.finditer(texto2)

view(r)

#### 
regex = re.compile(r"(lenta)(mente)", re.IGNORECASE)

r = regex.sub(r"\2", texto2)

print(r)
