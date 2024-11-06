def fib_it(n):
    if(n<=0):
        print("No seq possible")
    elif(n==0):
        print(0)
        return 0
    elif(n==1):
        print(0)
        print(1)
        return 1
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c
    return b
    
def fib_rec(n):
    if(n<=0):
        return 0
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    return fib_rec(n-1)+ fib_rec(n-2)
    
def print_fib_rec(n):
    if(n<=0):
        print("No seq possible")
    else:
        for i in range(1,n+1):
            print(fib_rec(i))
        
n=int(input("Enter the number:"))
print("The fibonacci seq using iterative is:")
fib_it(n);

print("The fibonacci seq using recurssive is:")
print_fib_rec(n)
