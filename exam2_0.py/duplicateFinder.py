#
#9. **Find Duplicate Elements in a List**
#   Input: `[1,2,3,2,4,3,5]` → Output: `[2,3]`

thelist = [1,2,3,2,4,3,5]
uniqueList = []
for x in thelist:
    if x not in uniqueList:
        uniqueList.append(x)
        
print("the old list: ", thelist)
print("the unique list: ", uniqueList)
