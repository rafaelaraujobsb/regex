import re

lista = """
    Lista telef:
        - (11) 98756-1212
        - 98765-5541
        - (12) 98254-1210
"""

regex = re.compile(r"\(?\d{0,2}\)?\s?\d{5}\-\d{4}")

print(re.findall(regex, lista))
