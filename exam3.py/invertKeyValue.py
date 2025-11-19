#Invert Key-Value Pairs
#Input: {"a": 1, "b": 2, "c": 3}
#Output: {1: "a", 2:"b", 3:"c"}
theInput = {"a": 1, "b": 2, "c": 3}
output = {}
for x, y in theInput.items():
    output[y] = x
print(output)

