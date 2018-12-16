import re

texto = """
Leo é muito legal
Emanuel foi jogar em Sergipe
Bianca é casada com Habib
"""

regex = re.compile(r"\n")

print(regex.findall(texto))

regex = re.compile(r"^(\w).+\1$", re.IGNORECASE) # Retorna None por conta do \n(não é um \w)

print(regex.findall(texto))

regex = re.compile(r"^(\w).+\1$", re.IGNORECASE|re.MULTILINE)

print([ match.group() for match in regex.finditer(texto) ])
