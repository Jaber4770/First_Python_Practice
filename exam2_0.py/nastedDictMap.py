# 20. **Invert Nested Dictionary Mapping**
#
#    ```
#    data = {"Dhaka": ["A","B"], "Chittagong": ["C"]}
#    Output: {"A":"Dhaka","B":"Dhaka","C":"Chittagong"}
#    ```
#
data = {"Dhaka": ["A", "B"], "Chittagong": ["C"]}
theDict = {}
for x in data:
    if x not in theDict:
        for y in data[x]:
            theDict[y] = x


print(theDict)