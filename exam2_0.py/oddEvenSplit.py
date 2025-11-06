#3. **Split List into Even and Odd Index Lists**
#   For a given list, create two new lists:

def splitList(lst):
    oddList = []
    evenList =[]
    for x in range(len(lst)):
        if x % 2 == 0:
            evenList.append(lst[x])
        else:
            oddList.append(lst[x])
            
    print('odd list: ', oddList)
    print('even list: ', evenList)

lst = [10, 20, 30, 40, 50, 60]
splitList(lst)
