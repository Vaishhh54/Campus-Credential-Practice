import re
email = input("Eneter email")
pattern = r'^[A-Za-Z0-9+-_]+@+[a-z]+\.$'
res = re.match(pattern,email)
if res:
    print("valid")
else:
    print("Not valid")