import re

texto = "0,1,2,3,4,5,6,7,8,9,a,b,c,e,f"

regex = re.compile('9')

match = re.search(regex, texto)

print("Posicoes: %s, %s; Valor %s" %(match.start(), match.end(), match.group(0)))

valores = re.findall('[a-z]', texto)

print(valores)
