# 19. **Create a Frequency Dictionary from List of Tuples**
#    Example input: `[("A",10),("B",20),("A",5)]`
#    Output: `{"A":15,"B":20}`
#
theTuple = [("A", 10),("B",20),("A",5)]
theDict = {}
for x in theTuple:
    theLetter = x[0]
    theValue = x[1]
    if theLetter not in theDict:
        theDict[theLetter] = theValue
    else:
        theDict[theLetter] += theValue
        
print("the dict: ", theDict)