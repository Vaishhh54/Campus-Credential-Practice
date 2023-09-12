num = int(input("Enter number"))
num1 = num
sum = 0
count=len(str(num))
while(num>0):
    rem = num%10
    sum = sum + rem**count
    num = num//10
if(sum==num1):
    print("number is amstrong number")
else:
    print("number is not amstrong number")

