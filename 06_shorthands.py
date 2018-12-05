import re


texto = """1,2,3,4,5,6,a.b c!d?e\r	-
f_g"""

print(re.findall("\d", texto)) # números [0-9]
print(re.findall("\D", texto)) # caracteres [a-zA-Z0-9_]
print(re.findall("\W", texto)) #  espaço [ \t\n\r\f]
print(re.findall("\S", texto)) # não espaço [^ \t\n\r\f]
