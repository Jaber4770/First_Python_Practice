#12. **Count Frequency of Elements**
#    Given a list, create a dictionary showing how many times each element occurs.
#theList = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,3,2,1,6,5,7,8,7,9,7,6,5,4,3,4,5,6,7,3]
theList = ['apple','apple','ball','cat','dog','dog','egg','dog','fall']
count = {}
for x in theList:
    if x not in count:
        count[x]=1
    else:
        count[x] += 1
print(count)
