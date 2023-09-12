n = int(input("Enter number"))
flag = False
if(n==1):
    print(n,"is not prime number")
elif(n>1):
    for i in range(2,n):
        if(n%i!=0):
            flag = True
            break
    if (flag==True):
        print("number is prime")
    else:
        print("number is not prime")      