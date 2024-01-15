def  swaplist(newList):
    size=len(newList)

    temp=newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp

    return newList

newList=[12,34,58,20,15]
print(swaplist(newList))
