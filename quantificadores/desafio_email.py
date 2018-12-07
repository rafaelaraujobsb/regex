import re

lista = """
    Lista emails:
    - fulano@cod3r.com.br
    - xico@gmail.com
    - joao@empresa.info.br
    - maria_silva@registro.br
    - rafa.sampaio@yahoo.com
"""

regex = re.compile(r"[A-z0-9]+@[A-z0-9]+\.[A-z]{2,4}")

print(re.findall(regex, lista))
