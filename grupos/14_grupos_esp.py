import re

texto = "João é calmo, mas no transito fica nervoso."

regex = re.compile(r"[\wÀ-ú]+", re.IGNORECASE)

r = regex.findall(texto)

print(r)

# Positive lookahead, olha para frente e seleciona o que está atrás
regex = re.compile(r"[\wÀ-ú]+(?=,)", re.IGNORECASE)

r = regex.findall(texto)

# calmo é a única palavra que tem uma vírgula na frente
print(r)

# Negative lookahead
regex = re.compile(r"[\wÀ-ú]+[\s|\.](?!,)", re.IGNORECASE)

r = regex.findall(texto)

print(r)