cost_price = int(input("Enter cost price: "))
ans = str(input("are you student: y/n"))
if(ans=='y or Y'):
    if(cost_price>=500):
        print("Cost price: ",cost_price)
        discount_price = (cost_price+((10*cost_price)/100))
        print("discount_price is:" ,discount_price)
    else:
        print("Cost price: "+cost_price)
        discount_price = (cost_price+((15*cost_price)/100))
        print(" discount_price is :" ,discount_price)
else:
        if(cost_price>=800):
            print("Cost price: ",cost_price)
            discount_price = (cost_price+((8*cost_price)/100))
            print("discount_price is:" , discount_price)
        else:
            print("Cost price: "+cost_price)
            discount_price =(cost_price+((2*cost_price)/100))
            print("discount_price is :" , discount_price)
    