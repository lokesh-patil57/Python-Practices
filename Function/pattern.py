n = int(input("Enter number : "))
def pattern(n):
    if (n == 0 ):
        return 
    print("*"*n)
    pattern(n-1)

pattern(n)