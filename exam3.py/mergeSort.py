# Merge and Sort Two Lists
# Given two lists, merge and sort them in ascending order.
list1 = [1, 2, 30, 4, 50, 6, 7, 8, 90, 10]
list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 110]
finalList = list1 + list2
print(finalList)
sortedFinalList = []

for i in range(len(finalList)):
   currentLarge = finalList[0]
   for x in finalList:
        if currentLarge > x:
            currentLarge = x
   sortedFinalList.append(currentLarge)
   finalList.remove(currentLarge)

print(f"merge and sorted list is: {sortedFinalList}")
