import re

result = 0

texto = open('text.txt')
linea = texto.read()

numbers = re.findall('[0-9]+', linea)

for i in numbers:
    result += int(i)

print(result)

