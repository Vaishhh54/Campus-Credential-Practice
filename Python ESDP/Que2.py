string1 = str(input("Enter String:  "))
rev = ''
n = (len(string1)) 
for i in range(n,0,-1):
    rev += string1[i-1]
print(rev)
if(rev==string1):
    print("String is palindrome")
else:
    print("String is not palindrome")