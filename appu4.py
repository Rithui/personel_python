#it is the code to find the max in the given list 
def maxi(list,a,b):
    if a>b:
        return a
    elif b<a:
        return b
    else:
        print("lnvalid input")

list=[36,89,90,30,28,78]
print("The given list is ",list)
pos1,pos2= input("Enter two positional values: ").split()
a=pos1
b=pos2
print('Max:',maxi(list,a-1,b-1))
        
