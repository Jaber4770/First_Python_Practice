# 10. **Flatten a Nested List (One Level)**
#    Example:
#
#    ```
#    Input: [[1,2], [3,4,5], [6]]
#    Output: [1,2,3,4,5,6]
#    ```
#
# ---

theList = [[1, 2], [3, 4, 5], [6]]
theNewList = []

for x in theList:
    for y in x:
        theNewList.append(y)

print("the old list: ", theList)
print("the new list: ", theNewList)
