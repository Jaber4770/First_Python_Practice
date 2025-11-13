#Reverse List Without reverse()
#Use a loop to reverse a list manually.
theList = [1,2,3,4,5,6,7,8,9,10,11,12,12,14,15,16,17]
reversedList = []
for x in range(len(theList) - 1, -1, -1):
    # print(theList[x])
    #print(x)
    reversedList.append(theList[x])

print(f"the reversed list is {reversedList}")