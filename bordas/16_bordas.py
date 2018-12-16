import re

# ^ -> inicio da linha/string
# $ -> fima da linha/string

texto = "Romário era um excelente jogador\n, mas hoje é um político questionador"

regex = re.compile(r"r", re.IGNORECASE) # todos os r

print(regex.findall(texto))

####

regex = re.compile(r"^r", re.IGNORECASE) 

print(regex.findall(texto))

####

regex = re.compile(r"r$", re.IGNORECASE) # retorna o r de questionador

print(regex.findall(texto))

####

regex = re.compile(r"^r.*r$", re.IGNORECASE) # . não resolve \n (problema dotall)

print(regex.findall(texto))
