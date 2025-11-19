# Frequency Counter (List)
#Count how many times each number appears in a list and print results(e.g. {2: 3, 3: 1, 5: 2}).
theList = [1, 2,3,4,5,6,7,8,9,10,1,2,3,4,3,2,1,6,5,7,8,7,9,7,6,5,4,3,4,5,6,7,3]
count = {}

for x in theList:
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1
print(count)