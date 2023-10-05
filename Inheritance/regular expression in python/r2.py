import re
pattern = r'\d+'
text = "watashiwa 123 no 456 desu"
match = re.search(pattern,text)
print(match)