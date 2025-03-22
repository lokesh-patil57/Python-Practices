n = int(input("Enter the number : "))
if(n==1):
            print("composite number")
elif(n < 0):
    print("Negative Number")
else :
    for i in range(2, n) :
        if (n%i) == 0 :
            print("Number is Not Prime")
            break
    else:
        print("Prime number")