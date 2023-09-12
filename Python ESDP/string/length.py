s = str(input("Enter a String"))
print(len(s))
print(s.count("a"))
#first way
print(s[::-1])
#second way
print(''.join(reversed(s)))
print(s.find("is"))
print(s.isalpha())