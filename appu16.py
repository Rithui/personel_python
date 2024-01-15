#it is the code for finding the GDC in given two inputs
def GCD(n,m):
    if n>m:
        small=n
    else:
        small=m

    for i in range(1,small+1):
        if(small%i==0 and small%i==0):
            gcd=i
        return gcd
            
        

n=int(input("enter the first number:"))
m=int(input("enter the second numebr:"))
print("The GCD of the given numbers are:",GCD(n,m))
