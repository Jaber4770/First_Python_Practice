#11. **Second Largest Element in a List**
#    Find the 2nd largest number without using sort().
theList = [1,2,3,4,5,6,7,8,9]
largest = second = -float('inf')
for num in theList:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
            second = num
print(largest,second)

