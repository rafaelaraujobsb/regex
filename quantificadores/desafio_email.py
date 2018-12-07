import re

lista = """
    Lista emails:
        - xyz@xc.bg
        - tarf@gmail.com
        - apple@apple.com
"""

regex = re.compile(r"\w+@{1}\w{2,9}\.com.?")

print(re.findall(regex, lista))
