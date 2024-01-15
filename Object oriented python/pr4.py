#Find Maximum of two numbers in Python
def maxi(numList):
    flag=0
    first=numList[0]
    for i in numList:
        if first<i:
            first=i
        return first

numList=[39,57,38,29,47,52,30]
print(numList)
print(maxi(numList))

            
    
