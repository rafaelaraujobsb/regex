import re

texto1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
texto2 = 'There is a big fog in NYC'

regex = re.compile(r"fogo+", re.IGNORECASE)
print(re.findall(regex, texto1))
print(re.findall(regex, texto2))

texto3 = 'Os números: 0123456789'

regex = re.compile(r"[0-9]")
print(re.findall(regex, texto3))
regex = re.compile(r"[0-9]+")
print(re.findall(regex, texto3))
