"""
Sum and Average of List
Input: list of numbers
Output: sum and average
"""
theList = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for x in theList:
    sum += x

average = sum / len(theList)
print("sum: ", sum)
print("average: ", average)
