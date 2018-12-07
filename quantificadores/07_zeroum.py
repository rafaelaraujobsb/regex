import re

texto1 = 'De longe eu avistei o fogo e uma pessoa gritando: FOGOOOOOO!'
texto2 = 'There is a big fog in NYC'

print(re.findall(r"fogo?", texto1))
print(re.findall(r"fogo?", texto2))
