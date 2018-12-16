import re

texto1 = "dia diatonico diafragma media wikipedia bom_dia melodia radial"

regex = re.compile(r"\bdia\w+", re.IGNORECASE)

print(regex.findall(texto1))

####

regex = re.compile(r"\w+dia\b", re.IGNORECASE)

print(regex.findall(texto1))

####

regex = re.compile(r"\w+dia\w+", re.IGNORECASE)

print(regex.findall(texto1))

####

texto2 = "dia diatônico diafragma, média wikipédia bom-dia melodia radial"

regex = re.compile(r"\bdia\b", re.IGNORECASE)

# no python caracter especial não é considerado borda
print(regex.findall(texto2))

####

regex = re.compile(r"(\S*)?dia(\S*)?", re.IGNORECASE)

# no python caracter especial não é considerado borda
print([ match.group() for match in regex.finditer(texto2) ])
