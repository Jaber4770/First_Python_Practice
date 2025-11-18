#Find Common Elements
#Input: two lists → output: elements that appear in both.

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9,10]
common = []
for x in list1:
    for y in list2:
        if x == y:
            common.append(x)
            
print("here is common elemnet from both list: ",common)