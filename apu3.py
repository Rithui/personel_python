#it is the code to swap two numbers in a given list ased of input pos
def swappy(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

list=[478,902,781,367,894,367]
pos1, pos2=1,5

print(swappy(list,pos1-1,pos2-1))

