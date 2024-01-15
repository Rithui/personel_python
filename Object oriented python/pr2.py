#Python Program to Swap Two Elements in a List
def swap(pos1,pos2,numList):
    temp=numList[pos1]
    numList[pos1]=numList[pos2]
    numList[pos2]=temp

    return numList

numList=[37,27,89,20,56]
print(numList)
pos1=int(input("Enter the pos1:"))
pos2=int(input("Enter the pos2:"))
pos1=pos1-1
pos2=pos2-1
print(swap(pos1,pos2,numList))
