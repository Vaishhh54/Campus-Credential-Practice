string1 = str(input("Enter String"))
rev = ''
n = (len(string1)) 
for i in range(n,0,-1):
    rev += string1[i-1]
print(rev)