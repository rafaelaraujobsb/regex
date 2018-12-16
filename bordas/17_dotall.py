import re

texto = "Romário era um excelente jogador\n, mas hoje é um político questionador"

regex = re.compile(r"^r[\s\S]*r$", re.IGNORECASE)

print(regex.findall(texto))

regex = re.compile(r"^r.*r$", re.IGNORECASE|re.DOTALL)

print(regex.findall(texto))