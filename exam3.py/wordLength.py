#Word Length Dictionary
#Input: ["apple", "banana", "cherry"]
#Output: {"apple": 5, "banana":6, "cherry":6}
theList = ["apple", "banana", "cherry"]
outPut = {}
for x in theList:
    length = len(x)
    outPut[x]=length
print(outPut)
