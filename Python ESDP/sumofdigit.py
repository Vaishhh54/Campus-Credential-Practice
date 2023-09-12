sum =0
num  = int(input("enter numnber"))
while num>0:
    rem = num%10
    sum = sum+rem
    num = num//10
print(sum)