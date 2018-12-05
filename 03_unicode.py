import re

texto = 'aʬc௵d'

print(re.findall(r"\u02AC|\u0BF5", texto))
