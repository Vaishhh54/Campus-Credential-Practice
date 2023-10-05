import re
pattern = r"I"
text = "I Love RCPIT"
match = re.findall(pattern,text)
print(match)