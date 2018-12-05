import re

texto = ".$+*?-"

print(re.search(r"[+.?*$]", texto))
print(re.search(r"[$-?]", texto)) # range de acordo com ASCII

print(re.search(r"[$\-?]", texto)) # não é um range
