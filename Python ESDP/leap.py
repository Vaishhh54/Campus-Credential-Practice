a = int(input("Enter year: "))
if(a%400==0):
    print("this century leap year")
elif((a%4==0) and (a%100 != 0)):
    print("non centuary year")
else:
    print("not leap year")