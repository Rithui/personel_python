#searching wether the elemnt is present in the list
numList=[47,28,903,82,745,29,68]
n=int(input("Enter the number:"))
r=0
for i in numList:
    if i==n:
        r=r+1


if r!=0:
    print("Element is present")
else:
    print("Element is not present")
