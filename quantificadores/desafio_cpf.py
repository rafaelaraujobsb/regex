import re

cpf = """
    CPF dos aprovados:
        - 125.689.412-56
        - 754.985.123-78
"""

regex = re.compile(r"\d{3}\.\d{3}\.\d{3}\-\d{2}")

print(re.findall(regex, cpf))
