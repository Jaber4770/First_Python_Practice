#Remove Duplicates
theList = [1, 2, 2, 3, 4, 4, 5, 5]
theUniqueList = []
for x in theList:
    if x not in theUniqueList:
        theUniqueList.append(x)
        
print(theUniqueList)

