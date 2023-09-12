marks1 = int(input("Enter marks"))
marks2 = int(input("Enter marks:"))
marks3 = int(input("Enter marks:"))
marks4 = int(input("Enter marks:"))
gender = input("Enter your gender")
marks = ((marks1+marks2+marks3+marks4)/400)*100
if(marks>=82 and gender=='f'):
    print("she is eligible for admission")

    
if(marks>=62 and gender=='m'):
    print("he is eligible for admission")

