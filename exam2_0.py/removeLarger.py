#8. **Remove Elements Greater Than a Given Value**
#   Given a list and a number x, remove all elements greater than x.

theList = [1,2,3,4,5,6,7,8,9,10,11,12,13,44,55,6,66,77,88,99,100]
givenNumber = 30
newList = []
for num in theList:
    if num<givenNumber:
        newList.append(num)
print("the old list: ",theList)
print("the new list: ",newList)

