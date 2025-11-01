#6. **Odd or Even Counter**
#   Count how many odd and even numbers are in a given list.
theList = [1,2,3,3,4,5,6,7,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
counter = {"even": 0, "odd": 0}
for x in theList:
    if x % 2 == 0:
        counter['even'] +=1
    else:
        counter['odd'] += 1
print(counter)

    