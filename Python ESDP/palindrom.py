rev=0
num = int(input("enter numnber"))
num1 =num
while num>0:
    rem=num%10
    rev = rev*10+rem
    num = num//10
if(num1== rev):
    print("Palindrome")
else:
    print("not palindrome")