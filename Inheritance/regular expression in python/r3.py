import re
pattern = r'\d{10}'
text = "watashiwa 12345612345 no 456 desu"
match = re.findall(pattern,text)
print(match)