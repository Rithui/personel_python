#How To Find the Length of a List in Python
def leng(numList):
    counter=0
    for i in numList:
         counter=counter+1
    return counter

numList=[39,29,16,57,48,90,20]
print(numList)
print(leng(numList))
