# Merge Two Dictionaries
# Combine two dictionaries into one(if same key → add values).

dict1 = {
    "apple": 5,
    "banana": 3
}
dict2 = {
    "apple": 2,
    "orange": 4
}
mergedDict = {}

for key in dict1:
    if key in dict2:
        mergedDict[key] = dict1[key] + dict2[key]
    else:
        mergedDict[key] = dict1[key]

print(f"the merded dict: {mergedDict}")
