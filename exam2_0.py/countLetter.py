#11. **Frequency of Characters in a String (Using Dict)**
#    Input: `"BANANA"` → Output: `{'B':1,'A':3,'N':2}`

theWord = "BANANA"
Count = {}
for x in theWord:
    if x not in Count:
        Count[x] = 1
    else:
        Count[x] += 1

print(theWord)
print(Count)
