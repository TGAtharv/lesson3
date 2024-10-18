num=int(input("Enter number to check:"))

if num>50:
    print("Number is greator than 50")
    if num%2==0:
        print("And it is even too")
        
    else:
        print("And it is odd")

else:
    print("Number is less than 50")