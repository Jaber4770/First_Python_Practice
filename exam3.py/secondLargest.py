#Second Largest Element
#Find the second largest number from a list(without sorting).
theList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 14, 15, 16, 17]
Largest = theList[0]
secondLargest = theList[0]
for x in theList:
    if Largest < x:
     Largest = x
for x in theList:
    if secondLargest < x and x != Largest:
        secondLargest = x
print(f"the largest is {Largest} and the second largest is {secondLargest}")
        

