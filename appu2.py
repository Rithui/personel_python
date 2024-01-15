#it is the code for swapping the fisrt and last digit of the given list of the numbers
def swaplist(newlist):
    size=len(newlist)

    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp


    return newlist


newlist=[36,89,26,78,56,47]
print(swaplist(newlist))
