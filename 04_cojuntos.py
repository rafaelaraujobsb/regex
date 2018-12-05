import re

# os conjuntos são declarados dentro de []

texto = '1,2,3,4,5,6,a.b c!d?e[f'

# Intervalos
print(re.findall(r"[a-z]", texto))
print(re.findall(r"[1-4]", texto))
print(re.findall(r"[A-Z1-3]", texto, flags=re.IGNORECASE))
