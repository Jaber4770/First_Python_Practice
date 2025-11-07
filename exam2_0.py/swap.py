#12. **Swap Keys and Values in a Dictionary**
#    Example:
#    `{"a":1, "b":2, "c":3}` → `{1:"a", 2:"b", 3:"c"}`

theDict = {"a":1, "b":2, "c":3}
swapDict = {}
for x in theDict:
    swapDict[theDict[x]] = x
    

print('the old dict: ', theDict)
print('the new dict: ', swapDict)