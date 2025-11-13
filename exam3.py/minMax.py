#Find Maximum and Minimum
#Print the largest and smallest number from a list without using max() or min().
theList = [1, 2,3,4,5,6,7,8,9,10]
print("the largest number is: ", max(theList))
print("the smallest number is: ", min(theList))

largest = theList[0]
smallest = theList[0]
for x in theList:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
print("the largest by loop is: ", largest)
print("the smallest by loop is: ", smallest)