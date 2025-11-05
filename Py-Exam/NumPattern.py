# 24. **Number Pattern Printing**
#    Print patterns like:
#    ```
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    ```
#def printNum(n):
#    for x in range(n):
#        for y in range(x):
#            print(y+1, end=" ")
#        print()
#    
#printNum(5)

for x in range(5):
    for y in range(x):
        print(y+1, end=" ")
    print()