# 16. **Reverse Dictionary**
#    Swap keys and values of a dictionary.
Dictionary = {
    "A": "Apple",
    "B": "Ball",
    "C": "Cat",
    "D": "Dog",
    "E": "Egg"
}
newDict = {}
for key, value in Dictionary.items():
    newDict[value] = key
print(newDict)
