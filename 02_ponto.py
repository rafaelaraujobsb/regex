import re

# O . é um coringa, lembrando que \n não é considerado pelo ponto

texto = "Bom dia"
texto2 = "Bom\ndia"

pattern = re.compile("m..i", re.IGNORECASE) # usado igual /i

print(re.search(pattern, texto))
print(re.search(pattern, texto2))
